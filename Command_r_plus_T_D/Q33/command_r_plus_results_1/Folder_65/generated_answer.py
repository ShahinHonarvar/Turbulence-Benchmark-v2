def return_vowels(input_string: str) -> list[str]:
    vowels = 'AEIOUaeiou'
    result = [char for char in input_string[71:88] if char in vowels and 9 < ord(char) <= ord('P')]
    return result