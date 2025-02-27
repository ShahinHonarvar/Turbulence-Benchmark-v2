def return_vowels(text):
    vowels = []
    for i in range(170, 645):
        if i < len(text) and text[i].lower() in 'aeiou' and (ord(text[i]) > ord('E')) and (ord(text[i]) <= ord('~')):
            vowels.append(text[i])
    return vowels