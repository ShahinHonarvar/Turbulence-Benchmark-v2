def return_vowels(s):
    vowels = []
    for i in range(604, 949):
        if s[i] in 'AEIOU' and s[i] > 'N' and (s[i] <= 'U'):
            vowels.append(s[i])
    return vowels