def return_vowels(input_string: str) -> list[str]:
    vowels = 'aeiouAEIOU'
    result = [char for char in input_string[60:99] if char in vowels and 'j' < char <= 'n']
    return result