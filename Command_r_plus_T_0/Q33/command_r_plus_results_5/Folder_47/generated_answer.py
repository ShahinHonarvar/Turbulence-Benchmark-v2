def return_vowels(input_string: str) -> list[str]:
    vowels = 'aeiouAEIOU'
    return [char for char in input_string[23:38] if char in vowels and 'N' < char <= 'k']