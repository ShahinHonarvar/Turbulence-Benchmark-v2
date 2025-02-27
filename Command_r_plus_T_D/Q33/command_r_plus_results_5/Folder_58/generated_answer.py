def return_vowels(input_string: str) -> list[str]:
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [char for char in input_string[260:322] if char.islower() and char in vowels and (char > '%') and (char <= 'U')]