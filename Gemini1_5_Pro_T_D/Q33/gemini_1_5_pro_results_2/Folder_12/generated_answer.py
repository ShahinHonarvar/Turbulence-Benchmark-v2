def return_vowels(text):
    vowels = []
    for i in range(13, 37):
        if i < len(text) and text[i] in 'aeiouAEIOU' and (ord(text[i]) > ord('Z')) and (ord(text[i]) <= ord('}')):
            vowels.append(text[i])
    return vowels