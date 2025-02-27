def return_vowels(s):
    vowels = 'aeiou'
    return [s[i] for i in range(1, 7) if s[i] in vowels and s[i] > 'F' and (s[i] <= 'j')]