def return_vowels(text):
    vowels = []
    for i in range(44, 95):
        if i < len(text) and ord(text[i]) > ord('5') and (ord(text[i]) <= ord('<')) and (text[i] in 'aeiouAEIOU'):
            vowels.append(text[i])
    return vowels