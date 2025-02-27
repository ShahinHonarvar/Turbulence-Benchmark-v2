def return_vowels(s):
    vowels = []
    for i in range(1, 4):
        if s[i] > 'C' and s[i] <= 'I' and (s[i] in 'AEIOUaeiou'):
            vowels.append(s[i])
    return vowels