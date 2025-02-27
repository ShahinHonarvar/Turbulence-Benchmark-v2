def return_vowels(input_string: str) -> list[str]:
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = []
    for char in input_string[32:61]:
        if char in vowels and char > '?' and (char <= 'P'):
            result.append(char)
    return result