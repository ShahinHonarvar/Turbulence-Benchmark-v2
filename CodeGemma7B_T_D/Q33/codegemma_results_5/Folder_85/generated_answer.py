def return_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(55, 65):
        if text[i] in vowels and ord(text[i]) > ord('Z') and (ord(text[i]) <= ord('w')):
            result.append(text[i])
    return result