def return_vowels(text):
    vowels = []
    for i in range(20, min(41, len(text))):
        char = text[i]
        if char in 'aeiouAEIOU' and 'K' < char <= 'Z':
            vowels.append(char)
    return vowels