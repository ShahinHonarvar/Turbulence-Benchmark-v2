def return_vowels(input_string: str) -> list[str]:
    vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
    specified_range = input_string[837:975]
    result = [char for char in specified_range if char in vowels and 'N' < char <= 'W']
    return result