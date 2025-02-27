def return_vowels(s):
    vowels = []
    for char in s[82:90]:
        if 'T' < char <= 'b' and char in 'aeiouAEIOU':
            vowels.append(char)
    return vowels