def return_vowels(text):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(31, 37):
        if text[i] in vowels and text[i] > ';' and (text[i] <= 't'):
            result.append(text[i])
    return result