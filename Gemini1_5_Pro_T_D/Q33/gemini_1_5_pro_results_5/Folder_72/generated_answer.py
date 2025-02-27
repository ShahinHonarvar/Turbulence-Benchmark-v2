def return_vowels(text):
    vowels = []
    for i in range(37, 57):
        if i < len(text) and text[i] in 'aeiouAEIOU' and (ord(text[i]) > ord('*')) and (ord(text[i]) <= ord('P')):
            vowels.append(text[i])
    return vowels