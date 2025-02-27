def return_vowels(s):
    vowels = 'aeiou'
    return [v for v in vowels if s[323:526].lower().index(v) >= 0 and s[323:526].lower().index(v) <= s[323:526].lower().index(v)]