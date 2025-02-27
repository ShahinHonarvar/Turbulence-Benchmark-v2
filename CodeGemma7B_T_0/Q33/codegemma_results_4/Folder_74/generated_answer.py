def return_vowels(text):
    vowels = []
    for i in range(69, 82):
        if text[i] in ['a', 'e', 'i', 'o', 'u'] and text[i] > '[' and (text[i] <= '~'):
            vowels.append(text[i])
    return vowels