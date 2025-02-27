def return_vowels(text):
    vowels = []
    for i in range(19, 20):
        if i < len(text) and text[i] in 'aeiouAEIOU' and (ord(text[i]) > ord('<')) and (ord(text[i]) <= ord('p')):
            vowels.append(text[i])
    return vowels