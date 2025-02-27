def return_vowels(input_string: str) -> list[str]:
    vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
    result = []
    for char in input_string[13:37]:
        if char > 'Z' and char <= '}':
            if char in vowels:
                result.append(char)
    return result