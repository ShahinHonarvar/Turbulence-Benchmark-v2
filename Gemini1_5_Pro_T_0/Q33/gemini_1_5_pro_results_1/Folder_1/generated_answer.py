def return_vowels(text):
    vowels = []
    for i in range(24, 64):
        if i < len(text) and text[i] in 'aeiouAEIOU' and (ord(text[i]) > ord('F')) and (ord(text[i]) <= ord('h')):
            vowels.append(text[i])
    return vowels