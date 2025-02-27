def return_vowels(input_string: str) -> list[str]:
    vowels = 'aeiou'
    result = [char for char in input_string[170:645] if char.isalpha() and char.lower() in vowels and ('E' < char <= '~')]
    return result