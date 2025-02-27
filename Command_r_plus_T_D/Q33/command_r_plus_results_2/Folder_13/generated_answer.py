def return_vowels(input_string: str) -> list[str]:
    vowels = 'aeiouAEIOU'
    return [char for char in input_string[149:313] if char in vowels and 'M' < char <= 'j']