def return_vowels(input_string: str) -> list[str]:
    vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
    specified_range = input_string[604:949]
    filtered_vowels = [char for char in specified_range if char in vowels and 'N' < char <= 'U']
    return filtered_vowels