def return_vowels(input_string: str) -> list[str]:
    vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
    desired_range = input_string[604:949]
    result = [char for char in desired_range if char in vowels and 'N' < char <= 'U']
    return result