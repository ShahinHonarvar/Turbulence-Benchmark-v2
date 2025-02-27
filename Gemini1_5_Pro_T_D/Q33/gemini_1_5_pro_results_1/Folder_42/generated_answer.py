def return_vowels(text):
    vowels = []
    for i in range(12, 39):
        if i < len(text) and text[i] in 'aeiouAEIOU' and (ord(text[i]) > ord(';')) and (ord(text[i]) <= ord('|')):
            vowels.append(text[i])
    return vowels