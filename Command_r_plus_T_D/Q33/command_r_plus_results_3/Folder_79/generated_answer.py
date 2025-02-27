def return_vowels(input_string: str) -> list[str]:
    vowels = 'AEIOUaeiou'
    start_index = 74
    end_index = 96
    return [char for char in input_string[start_index:end_index] if char in vowels and 'I' < char <= 'X']