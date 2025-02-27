def return_vowels(s):
    vowels = []
    for char in s[10:83]:
        if '%' < char <= 'e' and char in 'aeiouAEIOU':
            vowels.append(char)
    return vowels