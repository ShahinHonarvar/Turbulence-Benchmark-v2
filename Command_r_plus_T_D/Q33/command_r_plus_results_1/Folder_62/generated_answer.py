def return_vowels(input_string: str) -> list[str]:
    vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
    result = []
    for char in input_string[14:60]:
        if char in vowels and 'D' < char <= 'v':
            result.append(char)
    return result