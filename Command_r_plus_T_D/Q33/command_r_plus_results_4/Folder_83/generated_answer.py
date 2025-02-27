def return_vowels(input_string: str) -> list[str]:
    vowels = 'aeiou'
    result = [char for char in input_string[90:97] if char in vowels and char > '_' and (char <= 'x')]
    return result