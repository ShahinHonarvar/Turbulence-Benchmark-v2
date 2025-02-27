def return_vowels(s):
    vowels = 'aeiou'
    result = [c for c in s[273:275] if c in vowels and '+' < c <= 'o']
    return result