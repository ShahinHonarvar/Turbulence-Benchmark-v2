def return_vowels(text):
    vowels = []
    for i in range(14, min(60, len(text))):
        char = text[i]
        if char in 'aeiouAEIOU' and 'D' < char <= 'v':
            vowels.append(char)
    return vowels