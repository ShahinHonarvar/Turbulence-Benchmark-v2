def return_vowels(s):
    vowels = [s[i] for i in range(23, 57) if 'a' <= s[i] <= 'd' and s[i] in 'aeiou' and (s[i] > '\\x00')]
    return vowels