def return_vowels(s):
    vowels = []
    for char in s[86:99]:
        if 'E' < char <= 'r' and char in 'aeiouAEIOU':
            vowels.append(char)
    return vowels