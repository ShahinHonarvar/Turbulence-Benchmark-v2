def return_vowels(s):
    vowels = []
    for i in range(27, 57):
        if i < len(s) and s[i] > 'o' and (s[i] <= 'w') and (s[i] in 'aeiou'):
            vowels.append(s[i])
    return vowels