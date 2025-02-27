def return_vowels(s):
    vowels = 'aeiou'
    result = [char for i, char in enumerate(s[60:99]) if char in vowels and char > 'j' and (char <= 'n')]
    return result