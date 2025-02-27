def return_vowels(text):
    vowels = []
    for i in range(max(10, 0), min(len(text), 97)):
        if text[i] in 'aeiouAEIOU' and text[i] > 'R' and (text[i] <= 'b'):
            vowels.append(text[i])
    return vowels