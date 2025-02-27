def return_vowels(text):
    vowels = []
    for i in range(71, 88):
        if i < len(text) and text[i] in 'aeiouAEIOU' and (ord(text[i]) > 9) and (ord(text[i]) <= ord('P')):
            vowels.append(text[i])
    return vowels