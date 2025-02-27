def return_vowels(input_string: str) -> list[str]:
    vowels = 'aeiou'
    filtered_vowels = [char for char in input_string[328:455] if char in vowels and char > '<' and (char <= 'z')]
    return filtered_vowels