def return_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i, char in enumerate(text):
        if i >= 46 and i < 49 and (char in vowels) and (char > '[') and (char <= 'p'):
            result.append(char)
    return result