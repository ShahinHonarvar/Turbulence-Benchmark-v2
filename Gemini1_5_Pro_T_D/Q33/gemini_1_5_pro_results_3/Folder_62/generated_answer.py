def return_vowels(text):
    vowels = []
    for i in range(max(14, 0), min(60, len(text))):
        char = text[i]
        if char in 'aeiouAEIOU' and 'D' < char <= 'v':
            vowels.append(char)
    return vowels