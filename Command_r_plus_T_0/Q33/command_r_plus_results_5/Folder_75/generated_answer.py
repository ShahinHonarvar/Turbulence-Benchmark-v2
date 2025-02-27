def return_vowels(input_string: str) -> list[str]:
    vowels = 'AEIOUaeiou'
    result = [char for char in input_string[20:41] if char in vowels and 'K' < char <= 'Z']
    return result