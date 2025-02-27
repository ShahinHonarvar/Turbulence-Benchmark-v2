def return_vowels(s):
    return [c for c in s[604:949] if c in 'EOIU' and c > 'N' and (c <= 'U')]