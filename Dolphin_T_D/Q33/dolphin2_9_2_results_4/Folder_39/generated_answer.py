def return_vowels(s):
    vowels = 'aeiou'
    return [s[i] for i in range(32, 97) if s[i] in vowels and s[i] > 'Q' and (s[i] <= ']')]