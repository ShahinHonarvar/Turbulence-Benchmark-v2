def return_vowels(s):
    vowels = 'aeiou'
    result = [s[i] for i in range(63, 79) if s[i] in vowels and s[i] > 'D' and (s[i] <= 'y')]
    return result