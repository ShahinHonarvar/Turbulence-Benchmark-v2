def return_vowels(text):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    result = []
    for i in range(64, 82):
        if text[i].lower() in vowels and text[i] > 'P' and (text[i].lower() <= 'z'):
            result.append(text[i])
    return result