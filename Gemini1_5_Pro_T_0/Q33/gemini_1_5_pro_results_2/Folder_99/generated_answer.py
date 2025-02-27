def return_vowels(text):
    vowels = []
    for i in range(323, 526):
        if i < len(text) and text[i] in 'aeiouAEIOU' and (text[i] > '+') and (text[i] <= ':'):
            vowels.append(text[i])
    return vowels