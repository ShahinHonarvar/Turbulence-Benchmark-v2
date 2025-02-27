def return_vowels(s):
    vowels = 'aeiou'
    return [s[i] for i in range(46, 49) if s[i] in vowels and 'a' <= s[i] <= 'p']