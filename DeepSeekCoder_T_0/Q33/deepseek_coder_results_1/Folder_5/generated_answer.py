def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [c for c in s[44:95] if c in vowels and ord(c) > 53 and (ord(c) <= 76)]
    return result