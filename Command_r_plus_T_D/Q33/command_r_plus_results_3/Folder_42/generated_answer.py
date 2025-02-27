def return_vowels(input_string: str) -> list[str]:
    vowels = 'aeiou'
    start_index = 12
    end_index = 39
    valid_vowels = []
    for char in input_string[start_index:end_index]:
        if char in vowels and ';' < char <= '|':
            valid_vowels.append(char)
    return valid_vowels