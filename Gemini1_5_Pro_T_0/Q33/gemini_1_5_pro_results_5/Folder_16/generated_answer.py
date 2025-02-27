def return_vowels(text):
    vowels = []
    for i in range(133, 306):
        if i < len(text) and text[i] in 'aeiouAEIOU' and (ord(text[i]) > ord('c')) and (ord(text[i]) <= ord('d')):
            vowels.append(text[i])
    return vowels