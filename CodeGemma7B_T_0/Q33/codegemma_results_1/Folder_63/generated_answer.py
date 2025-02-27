def return_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(34, 69):
        if text[i] in vowels and text[i] > '_' and (text[i] <= 'o'):
            result.append(text[i])
    return result