def return_vowels(input_string: str) -> list[str]:
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = [char for char in input_string[40:91] if char.isalpha() and char.lower() in vowels and (char > 'A') and (char <= 'x')]
    return result