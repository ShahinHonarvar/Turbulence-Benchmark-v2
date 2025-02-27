def return_vowels(s):
    vowels = 'aeiou'
    return [s[i] for i in range(82, 90, 1) if 'T' < s[i] <= 'b' and s[i] in vowels]