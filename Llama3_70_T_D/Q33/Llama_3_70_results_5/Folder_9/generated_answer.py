def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [c for c in s[13:35] if c in vowels and ord(c) > 8 and (ord(c) <= 15)]