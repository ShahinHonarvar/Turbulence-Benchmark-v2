def return_vowels(input_string: str) -> list[str]:
    vowels = 'AEIOUaeiou'
    return [char for char in input_string[528:606] if char in vowels and 'M' < char <= 'X']