def return_vowels(input_string: str) -> list[str]:
    vowels = 'aeiouAEIOU'
    return [char for char in input_string[63:79] if char in vowels and 'D' < char <= 'y']