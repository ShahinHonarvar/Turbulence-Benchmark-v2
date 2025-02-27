def return_vowels(input_string: str) -> list[str]:
    vowels = ['A', 'E', 'I', 'O', 'U']
    filtered_vowels = [char for char in input_string[65:70] if char >= '%' and char <= 'G' and (char in vowels)]
    return filtered_vowels