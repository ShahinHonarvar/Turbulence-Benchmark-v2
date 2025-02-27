def return_vowels(input_string: str) -> list[str]:
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [char for char in input_string[1:5] if char in vowels and char > '!' and (char <= 'j')]
    return result