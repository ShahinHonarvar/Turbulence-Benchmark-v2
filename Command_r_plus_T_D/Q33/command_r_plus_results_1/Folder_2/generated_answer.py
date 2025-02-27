def return_vowels(input_string: str) -> list[str]:
    vowels = 'aeiou'
    filtered_vowels = [char for char in input_string[170:645] if char.isalpha() and char.lower() in vowels and (char > 'E') and (char <= '~')]
    return filtered_vowels