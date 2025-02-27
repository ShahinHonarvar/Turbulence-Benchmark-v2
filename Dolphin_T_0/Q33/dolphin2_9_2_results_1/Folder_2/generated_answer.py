def return_vowels(s):
    vowels = 'aeiou'
    return [c for c in s[170:645] if c in vowels and 'E' < c <= '~']