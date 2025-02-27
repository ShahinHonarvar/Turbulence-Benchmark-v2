def return_vowels(input_string: str) -> list[str]:
    vowels = 'AEIOUaeiou'
    return [char for char in input_string[13:37] if char in vowels and ord(char) > ord('Z') and (ord(char) <= ord('}'))]