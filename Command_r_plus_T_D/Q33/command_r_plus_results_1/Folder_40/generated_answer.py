def return_vowels(input_string: str) -> list[str]:
    vowels = 'aeiou'
    result = [char for char in input_string[2:7] if char in vowels and char > '^' and (char <= 'd')]
    return result