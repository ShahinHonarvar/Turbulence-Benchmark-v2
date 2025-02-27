def return_vowels(text):
    vowels = []
    for i in range(56, 96):
        if i < len(text) and text[i] in 'aeiouAEIOU' and (ord(text[i]) > ord('&')) and (ord(text[i]) <= ord('T')):
            vowels.append(text[i])
    return vowels