def return_vowels(s):
    vowels = 'aeiou'
    return [c for c in s[770:852] if c in vowels and c > 'B' and (c <= 'i')]