def return_vowels(input_string: str) -> list[str]:
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [char for char in input_string[54:82] if char >= '=' and char <= '@' and (char in vowels)]