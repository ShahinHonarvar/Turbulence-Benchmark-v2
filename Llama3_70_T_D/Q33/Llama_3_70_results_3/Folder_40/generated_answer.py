def return_vowels(s):
    vowels = []
    for char in s[2:7]:
        if char > '^' and char <= 'd' and (char in 'aeiouAEIOU'):
            vowels.append(char)
    return vowels