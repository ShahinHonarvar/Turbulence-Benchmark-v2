def return_vowels(text):
    vowels = []
    for i in range(170, 645):
        if i < len(text) and text[i] in 'aAeEiIoOuU' and (text[i] > 'E') and (text[i] <= '~'):
            vowels.append(text[i])
    return vowels