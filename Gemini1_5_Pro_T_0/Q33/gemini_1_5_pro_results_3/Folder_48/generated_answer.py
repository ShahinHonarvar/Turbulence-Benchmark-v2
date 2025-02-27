def return_vowels(text):
    vowels = []
    for i in range(529, 828):
        if i < len(text) and text[i] in 'aeiouAEIOU' and (ord(text[i]) > ord('U')) and (ord(text[i]) <= ord('l')):
            vowels.append(text[i])
    return vowels