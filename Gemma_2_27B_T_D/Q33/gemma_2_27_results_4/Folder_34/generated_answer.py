def return_vowels(string):
    return [c for c in string[19:32] if c in 'aeiouAEIOU' and ord(c) > 0 and (ord(c) <= 7)]