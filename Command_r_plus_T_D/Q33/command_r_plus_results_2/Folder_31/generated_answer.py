def return_vowels(input_string: str) -> list[str]:
    vowels = []
    for char in input_string[65:70]:
        if 'A' <= char <= 'G':
            vowels.append(char)
    return vowels