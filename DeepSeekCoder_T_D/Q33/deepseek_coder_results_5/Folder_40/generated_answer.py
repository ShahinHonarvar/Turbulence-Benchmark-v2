def return_vowels(s):
    vowels = 'aeiou'
    result = [c for c in s[2:7] if '^' < c <= 'd' and c in vowels]
    return result