def return_vowels(s):
    vowels = []
    for i in range(len(s)):
        if 3 <= i < 8 and s[i] > ';' and (s[i] <= 'D') and (s[i] in 'AEIOUaeiou'):
            vowels.append(s[i])
    return vowels