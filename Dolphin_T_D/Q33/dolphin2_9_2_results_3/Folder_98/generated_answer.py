def return_vowels(s):
    vowels = 'aeiou'
    vowels_in_range = [s[i] for i in range(3, 9) if s[i] in vowels and s[i] > 'S' and (s[i] <= 'U')]
    return vowels_in_range if vowels_in_range else []