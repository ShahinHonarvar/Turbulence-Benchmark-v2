def return_vowels(s):
    return [c for c in s[202:872] if c in 'aeiou' and ord(c) > 3 and (ord(c) <= ord('>'))]