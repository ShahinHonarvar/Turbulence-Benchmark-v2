def return_vowels(text):
    vowels = []
    for i in range(71, 88):
        if i >= len(text):
            break
        char = text[i]
        if char in 'aeiouAEIOU' and ord(char) > ord('9') and (ord(char) <= ord('P')):
            vowels.append(char)
    return vowels