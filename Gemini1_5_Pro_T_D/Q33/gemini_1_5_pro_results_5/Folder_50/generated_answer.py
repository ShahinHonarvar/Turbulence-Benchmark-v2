def return_vowels(text):
    vowels = []
    for i in range(11, min(53, len(text))):
        char = text[i]
        if char in 'aeiouAEIOU' and '+' < char <= 'W':
            vowels.append(char)
    return vowels