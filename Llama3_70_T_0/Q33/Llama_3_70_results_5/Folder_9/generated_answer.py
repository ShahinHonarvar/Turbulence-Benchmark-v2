def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [c for c in s[13:35] if c in vowels and 8 < ord(c) <= 15]