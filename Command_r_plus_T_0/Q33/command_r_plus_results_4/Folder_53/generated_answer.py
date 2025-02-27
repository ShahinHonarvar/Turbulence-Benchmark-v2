def return_vowels(input_string: str) -> list[str]:
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [char for char in input_string[27:57] if char in vowels and char > 'o' and (char <= 'w')]