def return_vowels(string):
    return [c for c in string[28:76] if c in 'aeiouAEIOU' and ord(c) > ord('+') and (ord(c) <= ord('z'))]