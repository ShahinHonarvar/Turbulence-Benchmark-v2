def return_vowels(text):
    vowels = []
    for i in range(47, 61):
        if text[i].lower() in 'aeiou' and ord(text[i]) > 9 and (ord(text[i]) <= ord('O')):
            vowels.append(text[i])
    return vowels