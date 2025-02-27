def return_vowels(input_string: str) -> list[str]:
    vowels = 'aeiouAEIOU'
    return [char for char in input_string[40:91] if char in vowels and 'A' < char <= 'x']