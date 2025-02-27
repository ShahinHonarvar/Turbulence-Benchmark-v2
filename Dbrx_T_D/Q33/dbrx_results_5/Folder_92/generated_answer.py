def return_vowels(s):
    vowels = []
    for char in s[3:8]:
        if 'a' <= char <= 'D' and char in 'aeiouAEIOU':
            vowels.append(char)
    return vowels