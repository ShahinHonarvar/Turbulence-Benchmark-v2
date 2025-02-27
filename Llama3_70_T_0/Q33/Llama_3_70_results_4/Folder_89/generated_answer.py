def return_vowels(s):
    vowels = []
    for char in s[50:51]:
        if ',' < char <= 'v' and char in 'aeiouAEIOU':
            vowels.append(char)
    return vowels