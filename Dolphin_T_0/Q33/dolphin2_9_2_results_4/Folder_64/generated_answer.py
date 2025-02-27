def return_vowels(s):
    vowels = 'aeiou'
    return [c for c in s[1:7] if vowels.count(c) > 0 and c > 'F' and (c <= 'j')]