def return_vowels(input_string: str) -> list[str]:
    vowels = 'AEIOUaeiou'
    specified_range = input_string[56:68]
    result = [char for char in specified_range if char in vowels and 'M' < char <= 'X']
    return result