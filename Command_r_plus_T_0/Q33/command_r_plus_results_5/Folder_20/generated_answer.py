def return_vowels(input_string: str) -> list[str]:
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [char for char in input_string[59:61] if char in vowels and char > '+' and (char <= 'h')]
    return result