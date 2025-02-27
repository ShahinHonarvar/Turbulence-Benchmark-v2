def return_vowels(text):
    vowels = []
    for i in range(70, 76):
        if i < len(text) and text[i] in 'aeiouAEIOU' and (ord(text[i]) > ord(text[2])) and (ord(text[i]) <= ord(':')):
            vowels.append(text[i])
    return vowels