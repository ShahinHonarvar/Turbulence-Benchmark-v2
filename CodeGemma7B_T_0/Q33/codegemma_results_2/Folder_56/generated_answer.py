def return_vowels(text):
    vowels = []
    for i in range(15, 86):
        if text[i].lower() in 'aeiou' and text[i] > '@' and (text[i] <= '~'):
            vowels.append(text[i])
    return vowels