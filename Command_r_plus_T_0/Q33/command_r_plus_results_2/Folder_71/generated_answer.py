def return_vowels(input_string: str) -> list[str]:
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [char for char in input_string[36:56] if char in vowels and char > '+' and (char <= '/')]
    return result