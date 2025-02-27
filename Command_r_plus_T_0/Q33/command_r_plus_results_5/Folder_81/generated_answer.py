def return_vowels(input_string: str) -> list[str]:
    vowels = 'aeiouAEIOU'
    return [char for char in input_string[20:43] if char in vowels and '5' < char <= 'M']