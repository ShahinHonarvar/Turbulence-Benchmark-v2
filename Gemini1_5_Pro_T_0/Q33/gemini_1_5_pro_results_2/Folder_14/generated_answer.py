def return_vowels(text):
    vowels = []
    for i in range(47, 61):
        if i >= len(text):
            break
        char = text[i]
        if char in 'aeiouAEIOU' and ord(char) > 9 and (ord(char) <= ord('O')):
            vowels.append(char)
    return vowels