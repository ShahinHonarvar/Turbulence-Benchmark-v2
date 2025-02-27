def return_vowels(text):
    vowels = []
    for i in range(171, 402):
        if i < len(text) and text[i] in 'aeiouAEIOU' and (ord(text[i]) > ord('I')) and (ord(text[i]) <= ord('k')):
            vowels.append(text[i])
    return vowels