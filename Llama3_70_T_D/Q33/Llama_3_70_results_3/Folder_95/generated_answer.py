def return_vowels(s):
    vowels = []
    for c in s[32:61]:
        if c > '?' and c <= 'P' and (c in 'aeiouAEIOU'):
            vowels.append(c)
    return vowels