def return_vowels(s):
    vowels = 'aeiou'
    result = [s[i] for i in range(60, 99) if s[i] in vowels and 'j' < s[i] <= 'n']
    return result