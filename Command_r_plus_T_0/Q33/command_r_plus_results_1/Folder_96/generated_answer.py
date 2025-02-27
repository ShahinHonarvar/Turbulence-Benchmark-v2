def return_vowels(input_string: str) -> list[str]:
    vowels = ['A', 'E', 'I', 'O', 'U']
    return [char for char in input_string[77:84] if char in vowels and ')' <= char <= 'G']