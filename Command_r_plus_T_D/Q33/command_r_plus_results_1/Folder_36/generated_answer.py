def return_vowels(input_string: str) -> list[str]:
    vowels = 'AEIOUaeiou'
    start_index = 604
    end_index = 949
    filtered_vowels = [char for char in input_string[start_index:end_index] if char in vowels and 'N' < char <= 'U']
    return filtered_vowels