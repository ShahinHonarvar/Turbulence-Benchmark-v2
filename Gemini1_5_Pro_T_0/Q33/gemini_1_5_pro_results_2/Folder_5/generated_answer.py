def return_vowels(text):
    vowels = []
    for i in range(44, 95):
        if i < len(text) and text[i] in 'aeiouAEIOU' and (ord(text[i]) > ord('5')) and (ord(text[i]) <= ord('<')):
            vowels.append(text[i])
    return vowels