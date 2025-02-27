def return_vowels(text):
    vowels = []
    for i in range(149, 313):
        if i < len(text) and text[i] in 'aeiouAEIOU' and (ord(text[i]) > ord('M')) and (ord(text[i]) <= ord('j')):
            vowels.append(text[i])
    return vowels