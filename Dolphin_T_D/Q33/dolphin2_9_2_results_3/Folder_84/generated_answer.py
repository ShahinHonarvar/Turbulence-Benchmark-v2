def return_vowels(s):
    vowels = 'aeiou'
    return [s[i] for i in range(770, 852) if s[i] in vowels and s[i] > 'B' and (s[i] <= 'i')]