def return_vowels(input_string: str) -> list[str]:
    vowels = 'aeiouAEIOU'
    desired_range = input_string[90:97]
    result = [char for char in desired_range if char in vowels and char > '_' and (char <= 'x')]
    return result