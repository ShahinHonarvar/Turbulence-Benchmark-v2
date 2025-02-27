def return_vowels(s):
    vowels = []
    for i in range(len(s)):
        if s[i] >= 'D' and s[i] <= 'y' and (i >= 63 and i < 79) and (s[i] in 'AEIOUaeiou'):
            vowels.append(s[i])
    return vowels