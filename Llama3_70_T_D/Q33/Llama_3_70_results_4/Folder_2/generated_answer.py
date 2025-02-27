def return_vowels(s):
    vowels = []
    for i in range(170, 645):
        if s[i] > 'E' and s[i] <= '~' and (s[i] in 'AEIOUaeiou'):
            vowels.append(s[i])
    return vowels