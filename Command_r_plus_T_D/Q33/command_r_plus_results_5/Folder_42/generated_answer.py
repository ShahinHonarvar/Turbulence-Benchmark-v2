def return_vowels(input_string: str) -> list[str]:
    vowels = 'aeiou'
    start_index = 12
    end_index = 39
    condition_min = ';'
    condition_max = '|'
    result = [char for char in input_string[start_index:end_index] if char in vowels and condition_min < char <= condition_max]
    return result