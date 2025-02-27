def return_vowels(s):
    return [x for x in s[12:39] if x in 'aeiouAEIOU' and ord(x) > ord(';') and (ord(x) <= ord('|'))]