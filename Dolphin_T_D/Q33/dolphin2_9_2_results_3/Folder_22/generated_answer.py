def return_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(56, 90):
        if text[i] in vowels:
            if text[i] > 'K' and text[i] <= 'z':
                result.append(text[i])
    return result