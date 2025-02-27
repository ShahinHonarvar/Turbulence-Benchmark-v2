def return_vowels(input_string: str) -> list[str]:
    vowels = 'aeiou'
    filtered_vowels = [char for char in input_string[43:70] if char in vowels and '*' < char <= 'b']
    return filtered_vowels