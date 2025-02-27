def return_vowels(s):
    vowels = []
    for i in range(31, 37):
        if i < len(s) and s[i] > ';' and (s[i] <= 't') and (s[i] in 'aeiou'):
            vowels.append(s[i])
    return vowels