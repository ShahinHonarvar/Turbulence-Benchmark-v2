def return_vowels(text):
    vowels = []
    for i in range(90, 97):
        if i < len(text) and text[i] in 'aeiouAEIOU' and (ord(text[i]) > ord('_')) and (ord(text[i]) <= ord('x')):
            vowels.append(text[i])
    return vowels