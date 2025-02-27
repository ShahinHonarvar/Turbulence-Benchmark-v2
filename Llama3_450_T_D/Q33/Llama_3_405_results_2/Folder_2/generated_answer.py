def return_vowels(s):
    vowels = 'AEIOUaeiou'
    return [c for i, c in enumerate(s[170:645]) if c in vowels and c > 'E' and (c <= '~')]