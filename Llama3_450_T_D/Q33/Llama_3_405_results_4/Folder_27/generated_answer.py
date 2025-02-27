def return_vowels(s):
    vowels = []
    for char in s[29:31]:
        if char > 'a' and char <= 'f' and (char in 'aeiou'):
            vowels.append(char)
    return vowels