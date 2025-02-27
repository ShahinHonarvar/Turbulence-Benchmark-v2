def return_vowels(text):
    vowels = []
    for i in range(55, 65):
        if i < len(text) and text[i] in 'aeiouAEIOU' and (ord(text[i]) > ord('Z')) and (ord(text[i]) <= ord('w')):
            vowels.append(text[i])
    return vowels