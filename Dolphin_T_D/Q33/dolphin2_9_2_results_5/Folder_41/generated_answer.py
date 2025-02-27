def return_vowels(s):
    vowels = 'aeiou'
    return [s[i] for i in range(71, 81) if '>' < s[i] <= 'U' and s[i] in vowels]