def return_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(13, 35):
        if text[i] in vowels and ord(text[i]) > 8 and (ord(text[i]) <= ord('F')):
            result.append(text[i])
    return result