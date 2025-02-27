def return_vowels(s):
    vowels = 'AEIOUaeiou'
    result = [c for c in s[170:645] if c in vowels and 'E' < c <= '~']
    return result