def return_vowels(s):
    vowels = []
    for i in range(29, 31):
        if i < len(s) and 'a' < s[i] <= 'f' and (s[i] in 'aeiou'):
            vowels.append(s[i])
    return vowels