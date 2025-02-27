def return_vowels(s):
    vowels = []
    for i in range(604, 949):
        if i < len(s) and 'N' < s[i] <= 'U' and (s[i] in 'AEIOU'):
            vowels.append(s[i])
    return vowels