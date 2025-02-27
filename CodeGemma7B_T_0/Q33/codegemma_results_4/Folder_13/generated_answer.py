def return_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(149, 313):
        if text[i] in vowels and text[i] > 'M' and (text[i] <= 'j'):
            result.append(text[i])
    return result