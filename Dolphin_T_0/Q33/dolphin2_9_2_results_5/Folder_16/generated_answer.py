def return_vowels(s, c, d):
    vowels = 'aeiou'
    return [i for i in s[133:306] if c < i <= d and i in vowels]