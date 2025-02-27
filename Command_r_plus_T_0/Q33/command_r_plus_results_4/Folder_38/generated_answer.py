def return_vowels(input_string: str) -> list[str]:
    vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
    result = []
    for char in input_string[17:65]:
        if char in vowels and 'U' < char <= '{':
            result.append(char)
    return result