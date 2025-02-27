def return_vowels(input_string: str) -> list[str]:
    vowels = 'aeiou'
    result = [char for char in input_string[328:455] if char in vowels and '>' in char <= 'z']
    return result