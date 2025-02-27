def return_vowels(s):
    vowels = 'aeiou'
    result = [s[i] for i in range(1, 4) if s[i] in vowels and s[i] > 'c' and (s[i] <= 'i')]
    return result