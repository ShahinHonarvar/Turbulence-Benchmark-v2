def return_vowels(text):
    vowels = []
    for i in range(71, 81):
        if i < len(text) and text[i] in 'AEIOUaeiou' and (ord(text[i]) > ord('>')) and (ord(text[i]) <= ord('U')):
            vowels.append(text[i])
    return vowels