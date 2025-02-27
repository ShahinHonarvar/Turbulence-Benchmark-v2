def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [c for i, c in enumerate(s[20:43]) if c in vowels and ord(c) > 5 and (ord(c) <= ord('M'))]