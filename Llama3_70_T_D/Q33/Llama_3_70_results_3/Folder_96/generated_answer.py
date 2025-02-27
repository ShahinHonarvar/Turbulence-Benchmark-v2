def return_vowels(s):
    vowels = 'AEIOUaeiou'
    result = [c for i, c in enumerate(s[77:84], 77) if c in vowels and '(' < c <= 'G']
    return result