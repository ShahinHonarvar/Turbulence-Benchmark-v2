def return_vowels(input_string: str) -> list[str]:
    vowels = 'aeiouAEIOU'
    return [char for char in input_string[45:76] if char in vowels and 'b' < char <= 'z']