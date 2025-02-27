def return_vowels(s):
    vowels = []
    for i in range(len(s)):
        if 528 <= i < 606 and 'M' < s[i] <= 'X' and (s[i] in 'AEIOU'):
            vowels.append(s[i])
    return vowels