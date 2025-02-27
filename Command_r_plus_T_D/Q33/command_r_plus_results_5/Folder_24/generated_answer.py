def return_vowels(input_string: str) -> list[str]:
    vowels = 'aeiouAEIOU'
    start_index = 23
    end_index = 57
    valid_vowels = [char for char in input_string[start_index:end_index] if char in vowels and '0' < char <= 'd']
    return valid_vowels