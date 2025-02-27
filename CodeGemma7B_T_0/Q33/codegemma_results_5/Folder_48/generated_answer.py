def return_vowels(text):
    vowels = []
    for i in range(529, 828):
        if text[i] in 'aeiouAEIOU' and text[i] > 'U' and (text[i] <= 'l'):
            vowels.append(text[i])
    return vowels