def return_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(14, 60):
        if text[i] in vowels and text[i] > 'D' and (text[i] <= 'v'):
            result.append(text[i])
    return result