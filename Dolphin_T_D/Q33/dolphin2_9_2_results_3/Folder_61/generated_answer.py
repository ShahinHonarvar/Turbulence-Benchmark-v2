def return_vowels(s):
    vowels = 'aeiou'
    return [v for v in s[1:4] if v in vowels and v > 'c' and (v <= 'i')]