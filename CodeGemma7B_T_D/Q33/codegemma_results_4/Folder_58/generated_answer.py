def return_vowels(text):
    vowels = ['A', 'E', 'I', 'O', 'U']
    valid_vowels = []
    for i in range(260, 322):
        if text[i] in vowels and text[i] > '%' and (text[i] <= 'U'):
            valid_vowels.append(text[i])
    return valid_vowels