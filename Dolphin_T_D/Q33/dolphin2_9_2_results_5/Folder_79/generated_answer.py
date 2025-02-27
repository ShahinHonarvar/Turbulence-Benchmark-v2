def return_vowels(s):
    vowels = 'aeiou'
    result = [s[i] for i in range(74, 96) if s[i] in vowels and 'i' < s[i] <= 'x']
    return result