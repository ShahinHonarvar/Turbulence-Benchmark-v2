def return_vowels(s):
    vowels = 'aeiou'
    filtered = [c for c in s[1:4] if vowels.count(c) and c > 'C' and (c <= 'I')]
    return filtered