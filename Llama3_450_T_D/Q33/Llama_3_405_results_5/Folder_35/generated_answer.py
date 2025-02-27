def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [c for c in s[483:664] if c in vowels and '&' < c <= 'h']