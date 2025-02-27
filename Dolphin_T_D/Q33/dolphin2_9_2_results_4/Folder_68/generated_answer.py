def return_vowels(s):
    vowels = 'aeiou'
    return [s[i] for i in range(1, 9) if s[i] in vowels and s[i] > '?' and (s[i] <= 'k')]