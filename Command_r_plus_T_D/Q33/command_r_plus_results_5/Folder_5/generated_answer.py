def return_vowels(input_string: str) -> list[str]:
    vowels = 'aeiouAEIOU'
    return [char for char in input_string[44:95] if char in vowels and 5 < ord(char) <= ord('<')]