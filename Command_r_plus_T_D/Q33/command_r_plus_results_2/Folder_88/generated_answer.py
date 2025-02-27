def return_vowels(input_string: str) -> list[str]:
    vowels = 'aeiouAEIOU'
    start_index = 70
    end_index = 76
    char_2 = '2'
    char_colon = ':'
    if start_index >= len(input_string) or end_index > len(input_string):
        return []
    valid_vowels = [char for char in input_string[start_index:end_index] if char in vowels]
    filtered_vowels = [vowel for vowel in valid_vowels if char_2 < vowel <= char_colon]
    return filtered_vowels