def return_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(24, 64):
        if text[i] in vowels and ord(text[i]) > ord('F') and (ord(text[i]) <= ord('h')):
            result.append(text[i])
    return result