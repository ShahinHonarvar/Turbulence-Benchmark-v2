def return_vowels(s):
    vowels = 'aeiou'
    result = [c for c in s[71:88] if c in vowels and '9' < c <= 'P']
    return result