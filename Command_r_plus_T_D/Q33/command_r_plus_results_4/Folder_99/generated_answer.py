def return_vowels(input_string: str) -> list[str]:
    vowels = 'aeiou'
    start_index = 323
    end_index = 526
    filtered_vowels = [char for char in input_string[start_index:end_index] if char in vowels and '+' < char <= ':']
    return filtered_vowels