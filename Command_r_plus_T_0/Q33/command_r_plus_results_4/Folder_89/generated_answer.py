def return_vowels(input_string: str) -> list[str]:
    vowels = ['a', 'e', 'i', 'o', 'u']
    filtered_vowels = [char for char in input_string[50:51] if char > ',' and char <= 'v' and (char in vowels)]
    return filtered_vowels