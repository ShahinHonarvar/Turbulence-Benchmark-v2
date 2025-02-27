def return_vowels(input_string: str) -> list[str]:
    vowels = ['a', 'e', 'i', 'o', 'u']
    filtered_vowels = [char for char in input_string[1:5] if char in vowels and '!' < char <= 'j']
    return filtered_vowels