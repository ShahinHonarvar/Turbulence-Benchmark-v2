def return_vowels(input_string: str) -> list[str]:
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    specified_range = input_string[50:51]
    result = [char for char in specified_range if char in vowels and ',' < char <= 'v']
    return result