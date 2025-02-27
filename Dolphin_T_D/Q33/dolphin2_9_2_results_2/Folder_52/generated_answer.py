def return_vowels(s):
    vowels = 'aeiou'
    return [s[i] for i in range(24, 68) if s[i] in vowels and s[i] > 'f' and (s[i] <= '|')]