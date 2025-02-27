def return_vowels(input_string: str) -> list[str]:
    vowels = 'aeiouAEIOU'
    return [char for char in input_string[4:8] if char in vowels and 'P' < char <= 'r']