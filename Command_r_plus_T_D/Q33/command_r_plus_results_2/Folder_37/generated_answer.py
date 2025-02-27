def return_vowels(input_string: str) -> list[str]:
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    specified_range = input_string[82:90]
    filtered_vowels = [char for char in specified_range if char in vowels and 'T' < char <= 'b']
    return filtered_vowels