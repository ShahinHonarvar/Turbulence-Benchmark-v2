def return_vowels(s):
    vowels = 'aeiou'
    result = [s[i] for i in range(495, 837) if s[i] in vowels and s[i] > 'B' and (s[i] <= 't')]
    return result