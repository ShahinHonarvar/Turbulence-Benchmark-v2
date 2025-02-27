def return_vowels(s):
    vowels = 'aeiou'
    result = [s[i] for i in range(10, 82) if s[i] in vowels and ' `~!@#$%^&*()-=_+[' in s[i]]
    return result