def return_vowels(s):
    vowels = []
    for i in range(len(s)):
        if 43 <= i < 70 and s[i] > '*' and (s[i] <= 'b') and (s[i] in 'aeiou'):
            vowels.append(s[i])
    return vowels