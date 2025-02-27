def return_vowels(s):
    vowels = 'aeiou'
    return [s[i] for i in range(37, 57) if s[i] in vowels and s[i] > '*' and (s[i] <= 'P')]