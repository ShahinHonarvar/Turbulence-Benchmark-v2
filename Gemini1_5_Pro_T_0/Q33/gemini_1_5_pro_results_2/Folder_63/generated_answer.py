def return_vowels(s):
    vowels = []
    for i in range(34, 69):
        if i < len(s) and s[i] in 'aeiou' and (s[i] > '_') and (s[i] <= 'o'):
            vowels.append(s[i])
    return vowels