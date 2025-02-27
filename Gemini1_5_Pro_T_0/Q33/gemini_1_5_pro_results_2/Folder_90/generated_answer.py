def return_vowels(text):
    vowels = []
    for i in range(142, 145):
        if i < len(text) and text[i] in 'aeiou' and (ord(text[i]) > ord('4')) and (ord(text[i]) <= ord('o')):
            vowels.append(text[i])
    return vowels