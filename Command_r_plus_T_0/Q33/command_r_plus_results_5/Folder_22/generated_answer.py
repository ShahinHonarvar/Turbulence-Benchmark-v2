def return_vowels(input_string: str) -> list[str]:
    vowels = 'aeiouAEIOU'
    return [char for char in input_string[56:90] if char in vowels and 'K' < char <= 'z']