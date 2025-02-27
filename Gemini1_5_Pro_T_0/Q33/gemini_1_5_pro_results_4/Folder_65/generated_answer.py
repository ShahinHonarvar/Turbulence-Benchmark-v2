def return_vowels(text):
    vowels = []
    for i in range(71, 88):
        if i < len(text) and 'a' <= text[i] <= 'z' and (text[i] in 'aeiou') and (9 < ord(text[i]) <= ord('P')):
            vowels.append(text[i])
    return vowels