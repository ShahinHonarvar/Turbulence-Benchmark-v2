def return_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(13, 37):
        if text[i] in vowels and ord(text[i]) > ord('Z') and (ord(text[i]) <= ord('{')):
            result.append(text[i])
    return result