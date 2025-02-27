def return_vowels(text):
    vowels = []
    for i in range(40, 94):
        if text[i] in 'aeiouAEIOU' and i > ord('4') and (ord(text[i]) <= ord('H')):
            vowels.append(text[i])
    return vowels