def return_vowels(input_string: str) -> list[str]:
    vowels = 'aeiou'
    start_index = 12
    end_index = 39
    desired_range = input_string[start_index:end_index]
    result = [char for char in desired_range if char in vowels and ';' < char <= '|']
    return result