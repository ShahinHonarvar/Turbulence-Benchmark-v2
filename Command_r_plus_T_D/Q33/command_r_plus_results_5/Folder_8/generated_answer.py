def return_vowels(input_string: str) -> list[str]:
    vowels = 'aeiou'
    filtered_vowels = [char for char in input_string[64:82] if char.islower() and char in vowels and (char > 'p') and (char <= 'z')]
    return filtered_vowels