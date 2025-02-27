def return_vowels(s):
    vowels = 'aeiou'
    return [s[i] for i in range(464, 574) if s[i] in vowels and 'a' < s[i] <= 'g']