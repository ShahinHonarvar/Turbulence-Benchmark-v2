def return_vowels(input_string: str) -> list[str]:
    vowels = 'aeiouAEIOU'
    result = [char for char in input_string[10:83] if char in vowels and char > '%' and (char <= 'e')]
    return result