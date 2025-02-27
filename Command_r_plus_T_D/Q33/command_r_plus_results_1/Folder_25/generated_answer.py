def return_vowels(input_string: str) -> list[str]:
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = []
    for char in input_string[28:76]:
        if char in vowels and '+' < char <= 'z':
            result.append(char)
    return result