def return_vowels(s):
    vowels = [c for c in s[12:39:1] if 'a' <= c <= 'e' or 'i' <= c <= 'o' or ('u' <= c <= 'u' and ';' < c <= '|')]
    return vowels