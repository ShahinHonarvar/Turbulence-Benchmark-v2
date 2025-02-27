def return_vowels(text):
    vowels = []
    for i in range(40, 94):
        if i < len(text) and text[i] in 'aeiouAEIOU' and (ord(text[i]) > ord('4')) and (ord(text[i]) <= ord('H')):
            vowels.append(text[i])
    return vowels