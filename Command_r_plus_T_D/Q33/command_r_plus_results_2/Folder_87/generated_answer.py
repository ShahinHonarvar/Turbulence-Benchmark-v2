def return_vowels(input_string: str) -> list[str]:
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [char for char in input_string[34:58] if char in vowels and char > 'b' and (char <= 'o')]