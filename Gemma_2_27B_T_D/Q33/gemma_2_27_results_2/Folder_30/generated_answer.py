def return_vowels(s):
    return [c for c in s[11:61] if c in 'EOIU' and c > 'M' and (c <= 'W')]