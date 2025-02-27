def return_vowels(input_string: str) -> list[str]:
    vowels = 'aeiou'
    result = []
    for char in input_string[13:37]:
        if char.isupper() and char > 'Z' and (char <= '}'):
            if char.lower() in vowels:
                result.append(char)
    return result