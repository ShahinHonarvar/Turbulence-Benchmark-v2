def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [c for i, c in enumerate(s[19:32], 19) if c in vowels and 0 < ord(c) <= 7]