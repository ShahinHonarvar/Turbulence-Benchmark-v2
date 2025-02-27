def return_vowels(s):
    return [c for c in s[529:828] if c > 'U' and c <= 'l' and (c in {'a', 'e', 'i', 'o', 'u'})]