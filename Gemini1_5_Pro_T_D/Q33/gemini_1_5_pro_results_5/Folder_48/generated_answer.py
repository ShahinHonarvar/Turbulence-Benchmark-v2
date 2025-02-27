def return_vowels(text):
    vowels = []
    for i in range(529, 828):
        if i < len(text) and text[i] in 'aeiou' and (text[i] > 'U') and (text[i] <= 'l'):
            vowels.append(text[i])
    return vowels