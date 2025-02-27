def return_vowels(s):
    vowels = []
    for char in s[46:50]:
        if 'a' < char <= 'p' and char in 'aeiou':
            vowels.append(char)
    return vowels