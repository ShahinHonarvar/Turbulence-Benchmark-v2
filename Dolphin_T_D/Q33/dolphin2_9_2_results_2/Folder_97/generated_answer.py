def return_vowels(s):
    vowels = 'aeiou'
    substring = s[328:455]
    res = [c for c in substring if c > '<' and c <= 'z' and (c in vowels)]
    return res