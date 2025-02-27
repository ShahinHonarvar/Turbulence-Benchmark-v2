def return_vowels(s):
    vowels = []
    for char in s[56:96]:
        if char > '&' and char <= 'T' and (char in 'aeiouAEIOU'):
            vowels.append(char)
    return vowels