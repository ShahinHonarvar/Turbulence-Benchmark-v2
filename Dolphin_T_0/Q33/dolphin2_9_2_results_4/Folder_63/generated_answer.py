def return_vowels(s):
    vowels = 'aeiou'
    return [s[i] for i in range(34, 69) if s[i] in vowels and s[i] > '_' and (s[i] <= 'o')]