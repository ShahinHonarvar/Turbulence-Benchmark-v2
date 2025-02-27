def return_vowels(text):
    vowels = []
    for i in range(202, 872):
        if i < len(text) and text[i] in 'aeiouAEIOU' and (ord(text[i]) > ord('3')) and (ord(text[i]) <= ord('>')):
            vowels.append(text[i])
    return vowels