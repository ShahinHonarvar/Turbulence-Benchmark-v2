def return_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    selected_vowels = []
    for i in range(len(text)):
        if text[i] in vowels and i >= 21 and (i < 59) and (text[i] > '/') and (text[i] <= 'a'):
            selected_vowels.append(text[i])
    return selected_vowels