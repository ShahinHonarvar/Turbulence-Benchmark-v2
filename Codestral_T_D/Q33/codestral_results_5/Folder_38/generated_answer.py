def return_vowels(s):
    return [c for c in s[17:65] if c > 'U' and c <= '{'] if {'a', 'e', 'i', 'o', 'u'}.intersection(set(s[17:65])) else []