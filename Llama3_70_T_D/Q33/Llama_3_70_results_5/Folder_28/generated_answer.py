def return_vowels(s):
    vowels = []
    s = s[41:50]
    for char in s:
        if char > 'W' and char <= '[' and (char in 'AEIOU'):
            vowels.append(char)
    return vowels