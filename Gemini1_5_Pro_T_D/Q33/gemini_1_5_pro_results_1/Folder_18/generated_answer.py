def return_vowels(text):
    vowels = []
    for i in range(528, 606):
        if i < len(text) and text[i] in 'AEIOU' and (ord(text[i]) > ord('M')) and (ord(text[i]) <= ord('X')):
            vowels.append(text[i])
    return vowels