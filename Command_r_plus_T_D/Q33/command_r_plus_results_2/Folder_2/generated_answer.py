def return_vowels(input_string: str) -> list[str]:
    vowels = ['I', 'U', 'i', 'u', 'y', 'Y']
    return [char for char in input_string[170:645] if char in vowels]