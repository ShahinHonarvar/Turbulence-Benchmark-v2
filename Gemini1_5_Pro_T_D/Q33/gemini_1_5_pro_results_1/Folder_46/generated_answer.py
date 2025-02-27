def return_vowels(text):
    vowels = []
    for i in range(max(10, 0), min(83, len(text))):
        if text[i] in 'aeiouAEIOU' and '%' < text[i] <= 'e':
            vowels.append(text[i])
    return vowels