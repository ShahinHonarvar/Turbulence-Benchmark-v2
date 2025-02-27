def return_vowels(s):
    vowels = [c for c in s[12:39] if 'a' <= c <= 'z' and c in 'aeiou' and (';' < c <= '|')]
    return vowels