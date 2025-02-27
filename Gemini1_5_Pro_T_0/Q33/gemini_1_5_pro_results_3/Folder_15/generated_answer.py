def return_vowels(text):
    vowels = []
    for i in range(5, 6):
        if i >= len(text):
            break
        char = text[i]
        if char in 'aeiouAEIOU' and ord(char) > ord(text[3]) and (ord(char) <= ord('^')):
            vowels.append(char)
    return vowels