def return_vowels(input_string: str) -> list[str]:
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [char for char in input_string[46:49] if char >= '[' and char <= 'p' and (char in vowels)]
    return result