def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [c for c in s[5:7] if ord(c) > 3 and ord(c) <= ord('^') and (c in vowels)]