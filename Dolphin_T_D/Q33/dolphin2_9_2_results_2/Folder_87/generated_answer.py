def return_vowels(s):
    vowels = 'aeiou'
    return [s[i] for i in range(34, 58) if 'b' < s[i] <= 'o' and s[i] in vowels]