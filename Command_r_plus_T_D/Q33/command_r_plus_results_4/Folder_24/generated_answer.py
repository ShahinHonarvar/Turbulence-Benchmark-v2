def return_vowels(input_string: str) -> list[str]:
    vowels = 'aeiouAEIOU'
    return [char for char in input_string[23:57] if char in vowels and '0' < char <= 'd']