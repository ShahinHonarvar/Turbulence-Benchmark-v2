def return_vowels(s):
    vowels = 'aeiou'
    result = [char for i, char in enumerate(s[46:49]) if char in vowels and '[' < char <= 'p']
    return result