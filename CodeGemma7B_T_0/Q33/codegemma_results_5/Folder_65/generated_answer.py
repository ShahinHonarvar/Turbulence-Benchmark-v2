def return_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(71, 88):
        if text[i] in vowels and (ord(text[i]) > 9 and ord(text[i]) <= ord('P')):
            result.append(text[i])
    return result