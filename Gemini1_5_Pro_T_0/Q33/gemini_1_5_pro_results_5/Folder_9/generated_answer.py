def return_vowels(text):
    vowels = []
    for i in range(13, 35):
        if i < len(text):
            char = text[i]
            if char in 'aeiouAEIOU' and ord(char) > 8 and (ord(char) <= ord('F')):
                vowels.append(char)
    return vowels