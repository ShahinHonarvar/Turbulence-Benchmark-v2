def return_vowels(input_string: str) -> list[str]:
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = []
    for char in input_string[163:771]:
        if char in vowels and char > ':' and (char <= 'E'):
            result.append(char)
    return result