def return_vowels(s):
    vowels = []
    for i in range(29, 31):
        if i < len(s) and (s[i] > 'a' and s[i] <= 'f' and (s[i] in 'aeiou')):
            vowels.append(s[i])
    return vowels