def return_vowels(s):
    vowels = 'aeiou'
    return [s[i] for i in range(11, 61) if s[i] in vowels and 'm' < s[i] <= 'w']