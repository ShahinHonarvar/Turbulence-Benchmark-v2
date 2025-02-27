def return_vowels(input_string: str) -> list[str]:
    vowels = 'aeiou'
    return [char for char in input_string[24:68] if char.islower() and char in vowels and ('f' < char <= '|')]