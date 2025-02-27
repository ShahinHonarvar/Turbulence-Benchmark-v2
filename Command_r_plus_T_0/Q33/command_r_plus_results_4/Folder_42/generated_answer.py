def return_vowels(input_string: str) -> list[str]:
    vowels = 'aeiou'
    result = []
    for char in input_string[12:39]:
        if char in vowels and char > ';' and (char <= '|'):
            result.append(char)
    return result