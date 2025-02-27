def return_vowels(input_string: str) -> list[str]:
    vowels = ['a', 'e', 'i', 'o', 'u']
    filtered_vowels = [char for char in input_string[77:84] if char >= '(' and char <= 'G' and (char in vowels)]
    return filtered_vowels