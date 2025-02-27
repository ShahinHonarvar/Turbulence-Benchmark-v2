def return_vowels(input_string: str) -> list[str]:
    vowels = 'aeiou'
    result = [char for char in input_string[28:76] if char.islower() and char in vowels]
    return result