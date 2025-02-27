def return_vowels(s):
    vowels = []
    for char in s[34:69]:
        if char > '_' and char <= 'o' and (char in 'aeiou'):
            vowels.append(char)
    return vowels