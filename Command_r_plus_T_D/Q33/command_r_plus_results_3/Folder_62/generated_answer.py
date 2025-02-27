def return_vowels(input_string: str) -> list[str]:
    vowels = 'aeiouAEIOU'
    result = [char for char in input_string[14:60] if char in vowels and 'D' < char <= 'v']
    return result