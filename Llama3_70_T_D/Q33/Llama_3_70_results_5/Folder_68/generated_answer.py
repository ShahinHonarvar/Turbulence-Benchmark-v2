def return_vowels(s):
    vowels = []
    for char in s[1:9]:
        if char > '?' and char <= 'k' and (char in 'aeiouAEIOU'):
            vowels.append(char)
    return vowels