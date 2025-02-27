def return_vowels(text):
    vowels = []
    for i in range(260, 322):
        if i < len(text) and text[i] in 'aeiouAEIOU' and (text[i] > '%') and (text[i] <= 'U'):
            vowels.append(text[i])
    return vowels