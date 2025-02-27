def return_vowels(text):
    vowels = []
    for i in range(51, 77):
        if i < len(text):
            if text[i] in 'aeiouAEIOU' and text[i] > '4' and (text[i] <= '='):
                vowels.append(text[i])
    return vowels