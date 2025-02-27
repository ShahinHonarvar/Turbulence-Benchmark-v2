def return_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(4, 8):
        if text[i] in vowels and 'p' < text[i] <= 'r':
            result.append(text[i])
    return result