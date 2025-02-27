def return_vowels(input_string: str) -> list[str]:
    vowels = 'aeiou'
    return [char for char in input_string[23:85] if char in vowels and 'W' < char <= 'v']