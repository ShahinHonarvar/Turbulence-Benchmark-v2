def return_vowels(s):
    vowels = []
    for char in s[3:9]:
        if char > 'S' and char <= 'U' and (char in 'AEIOU'):
            vowels.append(char)
    return vowels