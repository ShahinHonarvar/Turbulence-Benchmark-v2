def return_vowels(s):
    vowels = 'aeiou'
    return [s[i] for i in range(50, 77) if s[i] in vowels and '!' < s[i] < 'w']