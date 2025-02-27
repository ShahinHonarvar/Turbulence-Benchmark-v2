def return_vowels(input_string: str) -> list[str]:
    vowels = 'aeiou'
    result = [char for char in input_string[40:91] if char.lower() in vowels and 'A' < char <= 'x']
    return result