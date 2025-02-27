def return_vowels(input_string: str) -> list[str]:
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [char for char in input_string[3:8] if char in vowels and ord(char) > ord(';') and (ord(char) <= ord('D'))]