def return_vowels(text):
    vowels = []
    for i in range(51, 77):
        if i < len(text) and text[i] in 'aeiouAEIOU' and ('4' < text[i] <= '='):
            vowels.append(text[i])
    return vowels