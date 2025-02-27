def return_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(40, 94):
        if text[i] in vowels and text[i] > '4' and (text[i] <= 'H'):
            result.append(text[i])
    return result