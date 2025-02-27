def return_vowels(text):
    vowels = []
    for i in range(max(133, 0), min(306, len(text))):
        if text[i] in 'aeiouAEIOU' and 'c' < text[i] <= 'd':
            vowels.append(text[i])
    return vowels