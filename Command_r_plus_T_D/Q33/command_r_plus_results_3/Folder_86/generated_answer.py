def return_vowels(input_string: str) -> list[str]:
    vowels = ['a', 'e', 'i', 'o', 'u']
    specified_range = input_string[273:275]
    result = [char for char in specified_range if char in vowels and '+' < char <= 'o']
    return result