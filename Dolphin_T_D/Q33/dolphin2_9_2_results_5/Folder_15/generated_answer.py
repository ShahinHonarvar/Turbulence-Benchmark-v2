def return_vowels(s):
    vowels = []
    for char in s[5:6]:
        if char > '3' and char <= '^' and (char.lower() in 'aeiou'):
            vowels.append(char)
    return vowels