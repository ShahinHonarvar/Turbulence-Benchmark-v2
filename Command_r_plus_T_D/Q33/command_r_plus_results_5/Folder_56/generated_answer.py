def return_vowels(input_string: str) -> list[str]:
    vowels = 'aeiou'
    return [char for char in input_string[15:86] if char in vowels and '@' < char <= '~']