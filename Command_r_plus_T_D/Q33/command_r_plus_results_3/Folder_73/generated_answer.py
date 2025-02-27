def return_vowels(input_string: str) -> list[str]:
    vowels = 'aeiou'
    start_index = 47
    end_index = 89
    valid_vowels = [char for char in input_string[start_index:end_index] if char in vowels and char > '@' and (char <= 'n')]
    return valid_vowels