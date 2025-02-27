def return_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(41, 50):
        if text[i] in vowels and text[i] > 'W' and (text[i] <= '['):
            result.append(text[i])
    return result