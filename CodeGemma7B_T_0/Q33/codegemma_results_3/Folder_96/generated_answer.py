def return_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(77, 84):
        if text[i] in vowels and text[i] > ' ' and (text[i] <= 'G'):
            result.append(text[i])
    return result