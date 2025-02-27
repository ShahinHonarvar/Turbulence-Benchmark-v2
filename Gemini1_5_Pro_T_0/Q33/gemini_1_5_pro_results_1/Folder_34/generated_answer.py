def return_vowels(text):
    vowels = []
    for i in range(19, 32):
        if i < len(text) and 'a' <= text[i] <= 'z' and (text[i] in 'aeiou') and (ord(text[i]) > ord('0')) and (ord(text[i]) <= ord('7')):
            vowels.append(text[i])
    return vowels