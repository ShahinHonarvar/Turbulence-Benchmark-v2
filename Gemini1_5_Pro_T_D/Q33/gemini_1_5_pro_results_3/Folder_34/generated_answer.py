def return_vowels(text):
    vowels = []
    for i in range(19, 32):
        if i < len(text) and text[i] in 'aeiouAEIOU' and ('0' < text[i] <= '7'):
            vowels.append(text[i])
    return vowels