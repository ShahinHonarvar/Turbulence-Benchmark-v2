def return_vowels(input_string: str) -> list[str]:
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    filtered_vowels = [char for char in input_string[1:7] if char in vowels and 'F' < char <= 'j']
    return filtered_vowels