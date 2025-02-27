def return_vowels(text):
    vowels = []
    for i in range(max(10, 0), min(82, len(text))):
        if text[i] in 'aeiouAEIOU' and '$' < text[i] <= '@':
            vowels.append(text[i])
    return vowels