def return_vowels(s, c, d):
    vowels = 'aeiou'
    result = [s[i] for i in range(133, 306) if s[i] in vowels and c < s[i] <= d]
    return result