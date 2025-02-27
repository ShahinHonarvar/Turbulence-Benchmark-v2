def return_vowels(text):
    vowels = []
    for i in range(86, 99):
        if i < len(text) and text[i] in 'aeiouAEIOU' and (text[i] > 'E') and (text[i] <= 'r'):
            vowels.append(text[i])
    return vowels