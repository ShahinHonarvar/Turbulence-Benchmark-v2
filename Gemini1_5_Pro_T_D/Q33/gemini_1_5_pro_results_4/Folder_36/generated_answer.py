def return_vowels(text):
    vowels = []
    for i in range(604, 949):
        if i < len(text) and text[i].lower() in 'aeiou' and (ord(text[i]) > ord('N')) and (ord(text[i]) <= ord('U')):
            vowels.append(text[i])
    return vowels