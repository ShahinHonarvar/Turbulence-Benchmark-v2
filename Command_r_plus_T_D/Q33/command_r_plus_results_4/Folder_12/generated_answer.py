def return_vowels(input_string: str) -> list[str]:
    vowels = 'aeiou'
    start_index = 13
    end_index = 37
    valid_vowels = []
    for index in range(start_index, end_index):
        char = input_string[index]
        if char.isalpha() and char.lower() in vowels and ('Z' < char <= '}'):
            valid_vowels.append(char)
    return valid_vowels