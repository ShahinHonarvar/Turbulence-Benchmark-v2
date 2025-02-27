def return_vowels(text):
    vowels = []
    for i in range(82, 90):
        if i < len(text) and text[i] in 'aeiouAEIOU' and (text[i] > 'T') and (text[i] <= 'b'):
            vowels.append(text[i])
    return vowels