def return_vowels(s):
    vowels = 'aeiou'
    return [s[i] for i in range(56, 96) if '&' < s[i] <= 'T' and s[i] in vowels]