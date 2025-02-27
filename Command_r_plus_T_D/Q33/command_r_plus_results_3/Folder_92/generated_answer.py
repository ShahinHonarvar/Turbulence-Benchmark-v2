def return_vowels(input_string: str) -> list[str]:
    vowels = 'AEIOUaeiou'
    start_index = 3
    end_index = 8
    return [char for char in input_string[start_index:end_index] if char in vowels and ';' < char <= 'D']