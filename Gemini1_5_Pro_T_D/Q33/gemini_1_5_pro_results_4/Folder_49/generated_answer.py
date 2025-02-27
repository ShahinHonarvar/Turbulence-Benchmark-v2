def return_vowels(text):
    vowels = []
    for i in range(10, 97):
        if i < len(text) and text[i] in 'aeiouAEIOU' and (text[i] > 'R') and (text[i] <= 'b'):
            vowels.append(text[i])
    return vowels