def return_vowels(s):
    vowels = []
    for i in range(len(s)):
        if i >= 54 and i < 82 and ('e' < s[i] <= '@') and (s[i] in 'AEIOU'):
            vowels.append(s[i])
    return vowels