def return_vowels(input_string: str) -> list[str]:
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    desired_range = input_string[495:837]
    filtered_vowels = [char for char in desired_range if char in vowels and 'B' < char <= 't']
    return filtered_vowels