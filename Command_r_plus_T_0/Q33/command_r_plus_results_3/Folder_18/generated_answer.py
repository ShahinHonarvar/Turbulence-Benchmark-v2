def return_vowels(input_string: str) -> list[str]:
    vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
    filtered_vowels = [char for char in input_string[528:606] if char in vowels and 'M' < char <= 'X']
    return filtered_vowels