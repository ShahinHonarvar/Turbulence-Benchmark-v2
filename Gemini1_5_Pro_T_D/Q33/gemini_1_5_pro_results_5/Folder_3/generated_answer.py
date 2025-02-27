def return_vowels(text):
    vowels = []
    for i in range(50, 77):
        if i < len(text) and text[i] in 'aeiouAEIOU' and (ord(text[i]) > ord('#')) and (ord(text[i]) <= ord('r')):
            vowels.append(text[i])
    return vowels