def return_vowels(input_string: str) -> list[str]:
    vowels = 'aeiou'
    return [char for char in input_string[22:82] if char in vowels and 'N' < char <= 'o']