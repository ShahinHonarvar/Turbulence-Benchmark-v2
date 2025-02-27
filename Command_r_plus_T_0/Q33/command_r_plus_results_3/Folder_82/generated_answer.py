def return_vowels(input_string: str) -> list[str]:
    vowels = ['I', 'O', 'U']
    return [char for char in input_string[86:99] if char in vowels]