def return_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(1, 9):
        if text[i] in vowels and text[i] > '?' and (text[i] <= 'k'):
            result.append(text[i])
    return result