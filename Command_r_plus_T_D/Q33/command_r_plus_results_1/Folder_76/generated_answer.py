def return_vowels(input_string: str) -> list[str]:
    vowels = 'aeiouAEIOU'
    return [char for char in input_string[495:837] if char in vowels and 'B' < char <= 't']