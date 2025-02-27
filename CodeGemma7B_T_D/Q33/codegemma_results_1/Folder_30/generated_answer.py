def return_vowels(text):
    vowels = ['A', 'E', 'I', 'O', 'U']
    selected_vowels = []
    for i in range(11, 61):
        if text[i].upper() in vowels and text[i] > 'M' and (text[i] <= 'W'):
            selected_vowels.append(text[i])
    return selected_vowels