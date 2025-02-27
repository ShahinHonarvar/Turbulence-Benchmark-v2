def return_vowels(input_string: str) -> list[str]:
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in input_string[273:275]:
        if '+' < char <= 'o' and char in vowels:
            result.append(char)
    return result