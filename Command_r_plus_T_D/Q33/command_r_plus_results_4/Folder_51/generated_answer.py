def return_vowels(input_string: str) -> list[str]:
    vowels = 'AEIOUaeiou'
    result = [char for char in input_string[56:68] if char in vowels and 'M' < char <= 'X']
    return result