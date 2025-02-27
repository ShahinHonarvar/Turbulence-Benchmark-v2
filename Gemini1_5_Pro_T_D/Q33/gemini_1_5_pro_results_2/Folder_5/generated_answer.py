def return_vowels(text):
    vowels = []
    for i in range(44, 95):
        if i >= len(text):
            break
        char = text[i]
        if char in 'aeiouAEIOU' and ord(char) > ord('5') and (ord(char) <= ord('<')):
            vowels.append(char)
    return vowels