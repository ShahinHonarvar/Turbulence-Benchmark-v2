def return_vowels(input_string: str) -> list[str]:
    vowels = 'aeiouAEIOU'
    result = []
    for char in input_string[32:97]:
        if char in vowels and 'Q' < char <= ']':
            result.append(char)
    return result