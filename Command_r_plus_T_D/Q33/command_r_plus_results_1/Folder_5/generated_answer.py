def return_vowels(input_string: str) -> list[str]:
    vowels = 'aeiou'
    return [char for char in input_string[44:95] if char.lower() in vowels and 5 < ord(char) <= ord('<')]