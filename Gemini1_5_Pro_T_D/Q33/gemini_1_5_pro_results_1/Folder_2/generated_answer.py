def return_vowels(string):
    vowels = []
    for i in range(170, 645):
        if i < len(string) and string[i] in 'aeiouAEIOU' and ('E' < string[i] <= '~'):
            vowels.append(string[i])
    return vowels