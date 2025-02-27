def return_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(3, 9):
        if text[i] in vowels and text[i] > 'S' and (text[i] <= 'U'):
            result.append(text[i])
    return result