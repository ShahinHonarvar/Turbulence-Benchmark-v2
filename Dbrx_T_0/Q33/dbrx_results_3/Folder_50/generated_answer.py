def return_vowels(s):
    vowels = []
    for i in range(11, 53):
        if s[i] > '+' and s[i] <= 'W' and (s[i] in 'AEIOUaeiou'):
            vowels.append(s[i])
    return vowels