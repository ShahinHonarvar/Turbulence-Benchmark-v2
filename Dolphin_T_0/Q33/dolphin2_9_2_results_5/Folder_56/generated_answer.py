def return_vowels(s):
    vowels = 'aeiou'
    result = [c for c in s[15:86] if c in vowels and '@' < c <= '~']
    return result