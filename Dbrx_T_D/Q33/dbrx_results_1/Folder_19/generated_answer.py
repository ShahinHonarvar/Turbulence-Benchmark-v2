def return_vowels(s: str) -> list:
    vowels = [c for c in s[51:77] if 4 < ord(c) <= ord('=') and c in 'AEIOU']
    return vowels