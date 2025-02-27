def return_vowels(s):
    vowels = 'aeiou'
    return [s[i] for i in range(529, 828) if s[i] in vowels and 'U' < s[i] <= 'l']