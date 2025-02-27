def return_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(45, 76):
        if text[i] in vowels and text[i] > 'b' and (text[i] <= 'z'):
            result.append(text[i])
    return result