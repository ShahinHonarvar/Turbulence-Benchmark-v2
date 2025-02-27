def return_vowels(s):
    vowels = []
    for i in range(56, 90):
        if s[i].lower() > 'k' and s[i].lower() <= 'z' and (s[i] in 'aeiouAEIOU'):
            vowels.append(s[i])
    return vowels