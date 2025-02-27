def return_vowels(s):
    vowels = [c for c in s[202:872] if c.lower() in 'aeiou' and 3 < ord(c) <= ord('>')]
    return vowels or []