def return_vowels(s):
    vowels = []
    for char in s[31:37]:
        if char > ';' and char <= 't' and (char in 'aeiouAEIOU'):
            vowels.append(char)
    return vowels