def return_vowels(s):
    vowels = []
    for char in s[41:50]:
        if char > 'W' and char <= '[' and (char in 'AEIOUaeiou'):
            vowels.append(char)
    return vowels