def return_vowels(input_string: str) -> list[str]:
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = []
    for char in input_string[85:99]:
        if char in vowels and char >= '/' and (char <= 'n'):
            result.append(char)
    return result