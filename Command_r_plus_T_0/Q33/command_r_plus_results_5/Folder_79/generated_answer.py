def return_vowels(input_string: str) -> list[str]:
    vowels = ['A', 'E', 'I', 'O', 'U']
    return [char for char in input_string[74:96] if char in vowels and 'I' < char <= 'X']