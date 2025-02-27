def return_vowels(input_string: str) -> list[str]:
    vowels = 'aeiou'
    result = [char for char in input_string[21:59] if char in vowels and char >= '/' and (char <= 'a')]
    return result