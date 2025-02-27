def return_vowels(input_string: str) -> list[str]:
    vowels = ['a', 'e', 'i', 'o', 'u']
    filtered_vowels = [char for char in input_string[273:275] if char in vowels and '+' < char <= 'o']
    return filtered_vowels