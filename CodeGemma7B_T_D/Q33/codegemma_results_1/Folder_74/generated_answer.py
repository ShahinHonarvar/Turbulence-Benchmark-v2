def return_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(69, 82):
        if text[i] in vowels and text[i] > '[' and (text[i] <= '~'):
            result.append(text[i])
    return result