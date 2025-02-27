def return_vowels(input_string: str) -> list[str]:
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = [char for char in input_string[142:145] if char in vowels and ord(char) > 4 and (ord(char) <= ord('o'))]
    return result