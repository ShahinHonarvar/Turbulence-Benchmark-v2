def return_vowels(s):
    vowels = []
    for char in s[77:84]:
        if char > '(' and char <= 'G' and (char in 'AEIOU'):
            vowels.append(char)
    return vowels