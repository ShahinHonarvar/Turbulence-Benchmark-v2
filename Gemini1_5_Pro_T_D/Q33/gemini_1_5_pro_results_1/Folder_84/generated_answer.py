def return_vowels(text):
    vowels = []
    for i in range(770, 852):
        if i < len(text) and text[i] in 'aeiouAEIOU' and (ord(text[i]) > ord('B')) and (ord(text[i]) <= ord('i')):
            vowels.append(text[i])
    return vowels