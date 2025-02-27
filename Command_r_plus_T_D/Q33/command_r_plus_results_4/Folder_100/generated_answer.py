def return_vowels(input_string: str) -> list[str]:
    vowels = 'aeiouAEIOU'
    return [char for char in input_string[23:75] if char in vowels and 'L' < char <= 'd']