def return_vowels(s):
    vowels = []
    for char in s[8:9]:
        if 'Y' < char <= 's' and char in 'aeiouAEIOU':
            vowels.append(char)
    return vowels