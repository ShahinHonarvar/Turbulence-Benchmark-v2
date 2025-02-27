def return_vowels(text):
    vowels = []
    for i in range(10, min(82, len(text))):
        if text[i] in 'aeiouAEIOU' and '$' < text[i] <= '@':
            vowels.append(text[i])
    return vowels