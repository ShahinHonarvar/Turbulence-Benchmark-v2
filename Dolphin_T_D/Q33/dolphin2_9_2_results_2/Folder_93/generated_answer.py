def return_vowels(s):
    vowels = 'aeiou'
    return [s[i] for i in range(54, 82) if s[i] in vowels and '&' < s[i] <= '@']