def return_vowels(s):
    vowels = 'aeiou'
    return [s[i] for i in range(32, 61) if s[i] in vowels and s[i] > '?' and (s[i] <= 'P')]