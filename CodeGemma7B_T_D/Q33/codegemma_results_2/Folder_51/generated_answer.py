def return_vowels(text):
    vowels = []
    for i in range(56, 68):
        if text[i].lower() in ['a', 'e', 'i', 'o', 'u'] and text[i].lower() > 'm' and (text[i].lower() <= 'x'):
            vowels.append(text[i])
    return vowels