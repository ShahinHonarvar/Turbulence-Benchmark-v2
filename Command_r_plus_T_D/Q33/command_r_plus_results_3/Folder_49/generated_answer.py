def return_vowels(input_string: str) -> list[str]:
    vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
    result = []
    for char in input_string[10:97]:
        if char in vowels and char > 'R' and (char <= 'b'):
            result.append(char)
    return result