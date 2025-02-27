def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i, char in enumerate(string):
        if i >= 23 and i < 38 and (char in vowels) and (char > 'N') and (char <= 'k'):
            result.append(char)
    return result