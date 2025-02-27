def return_vowels(text):
    vowels = []
    for i in range(14, min(60, len(text))):
        char = text[i]
        if 'D' < char <= 'v' and char in 'aeiouAEIOU':
            vowels.append(char)
    return vowels