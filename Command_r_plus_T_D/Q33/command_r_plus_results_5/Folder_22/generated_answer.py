def return_vowels(input_string: str) -> list[str]:
    vowels = 'aeiou'
    desired_range = input_string[56:90]
    result = [char for char in desired_range if char in vowels and 'K' < char <= 'z']
    return result