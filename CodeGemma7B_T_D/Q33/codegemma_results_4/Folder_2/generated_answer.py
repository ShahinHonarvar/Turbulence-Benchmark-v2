def return_vowels(str):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(170, 645):
        if str[i] in vowels and str[i] > 'E' and (str[i] <= '~'):
            result.append(str[i])
    return result