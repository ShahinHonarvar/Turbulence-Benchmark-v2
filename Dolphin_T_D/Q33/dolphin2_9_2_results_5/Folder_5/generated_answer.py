def return_vowels(s):
    vowels = 'aeiou'
    return [s[i] for i in range(44, 95) if 5 < ord(s[i]) < ord('<') and s[i] in vowels]