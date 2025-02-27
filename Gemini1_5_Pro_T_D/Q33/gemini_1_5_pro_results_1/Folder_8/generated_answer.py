def return_vowels(text):
    vowels = []
    for i in range(64, 82):
        if text[i] in 'aeiou' and ord(text[i]) > ord('P') and (ord(text[i]) <= ord('z')):
            vowels.append(text[i])
    return vowels