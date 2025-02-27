def return_vowels(text):
    vowels = list('aeiouAEIOU')
    result = []
    for i in range(64, 82):
        if text[i] in vowels and text[i] > 'P' and (text[i] <= 'z'):
            result.append(text[i])
    return result