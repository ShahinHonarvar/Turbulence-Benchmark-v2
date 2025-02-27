def return_vowels(input_string: str) -> list[str]:
    vowels = 'aeiouAEIOU'
    start_index = 142
    end_index = 145
    valid_vowels = [char for char in input_string[start_index:end_index] if char in vowels and 4 < ord(char) <= ord('o')]
    return valid_vowels