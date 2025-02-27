def return_vowels(s):
    vowels = []
    for char in s[4:8]:
        if 'P' < char <= 'r' and char in 'aeiouAEIOU':
            vowels.append(char)
    return vowels