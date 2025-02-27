def return_vowels(input_string: str) -> list[str]:
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = []
    for char in input_string[1:9]:
        if char in vowels and char > '?' and (char <= 'k'):
            result.append(char)
    return result