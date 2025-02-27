def return_vowels(s):
    vowels = []
    for i in range(min(10, len(s)), min(97, len(s))):
        if s[i] > 'R' and s[i] <= 'b' and (s[i] in 'aeiouAEIOU'):
            vowels.append(s[i])
    return vowels