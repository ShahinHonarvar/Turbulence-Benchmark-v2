def return_vowels(s):
    return [i for i in s[5:6] if i in 'aeiouAEIOU' and ord(i) > 3 and (ord(i) <= ord('^'))]