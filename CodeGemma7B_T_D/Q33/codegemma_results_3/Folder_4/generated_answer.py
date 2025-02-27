def return_vowels(str):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i, char in enumerate(str):
        if i >= 40 and i < 91 and (char in vowels) and (char > 'A') and (char <= 'x'):
            result.append(char)
    return result