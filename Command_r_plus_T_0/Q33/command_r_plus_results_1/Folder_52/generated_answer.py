def return_vowels(input_string: str) -> list[str]:
    vowels = 'aeiouAEIOU'
    return [char for char in input_string[24:68] if char in vowels and 'f' < char <= '|']