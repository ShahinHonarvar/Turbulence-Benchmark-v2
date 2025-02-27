def return_vowels(s):
    vowels = []
    for i in range(163, 771):
        if s[i] > ':' and s[i] <= 'E' and (s[i] in 'AEIOUaeiou'):
            vowels.append(s[i])
    return vowels