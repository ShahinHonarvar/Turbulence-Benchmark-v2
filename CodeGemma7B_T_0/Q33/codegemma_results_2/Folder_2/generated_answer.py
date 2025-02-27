def return_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(170, 645):
        if text[i] in vowels and text[i] > 'E' and (text[i] <= '~'):
            result.append(text[i])
    return result