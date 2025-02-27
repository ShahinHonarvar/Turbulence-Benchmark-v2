def return_vowels(input_string: str) -> list[str]:
    vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
    result = [char for char in input_string[3:8] if char in vowels and ord(char) > ord(';') and (ord(char) <= ord('D'))]
    return result