def return_vowels(strg):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(24, 68):
        if strg[i] in vowels and strg[i] > 'f' and (strg[i] <= '|'):
            result.append(strg[i])
    return result