def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [c for c in s[23:57] if c in vowels and 0 < ord(c) <= ord('d')]