def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [c for c in s[47:61] if c in vowels and ord(c) > ord('9') and (ord(c) <= ord('O'))]