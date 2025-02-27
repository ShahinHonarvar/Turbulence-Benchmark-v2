def return_vowels(s):
    vowels = 'aeiou'
    output = [s[i] for i in range(23, 75) if s[i] > 'L' and s[i] <= 'd' and (s[i] in vowels)]
    return output