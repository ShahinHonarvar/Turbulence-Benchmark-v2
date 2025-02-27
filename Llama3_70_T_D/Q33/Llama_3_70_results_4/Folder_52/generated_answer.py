def return_vowels(s):
    vowels = [c for c in s[24:68] if 'a' <= c <= 'z' and c in 'aeiou' and (c > 'f') and (c <= '|')]
    return vowels