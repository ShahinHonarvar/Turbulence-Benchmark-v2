def return_vowels(s):
    vowels = [c for c in s[142:145] if 'aeiou'.count(c) == 1 and ord(c) > 4 and (ord(c) <= ord('o'))]
    return vowels