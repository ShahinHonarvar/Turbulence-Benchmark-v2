def return_vowels(s):
    vowels = 'aeiou'
    return [s[i] for i in range(171, 402) if s[i] in vowels and s[i] > 'I' and (s[i] <= 'k')]