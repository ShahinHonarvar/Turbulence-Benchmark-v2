def return_vowels(input_string: str) -> list[str]:
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = []
    for char in input_string[44:95]:
        if char in vowels and ord(char) > 5 and (ord(char) <= ord('<')):
            result.append(char)
    return result