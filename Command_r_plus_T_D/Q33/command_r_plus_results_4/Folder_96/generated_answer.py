def return_vowels(input_string: str) -> list[str]:
    vowels = ['A', 'E', 'I', 'O', 'U']
    filtered_vowels = [char for char in input_string[77:84] if char in vowels and 'G' >= char >= '(']
    return filtered_vowels