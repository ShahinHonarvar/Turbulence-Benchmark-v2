def return_vowels(s):
    vowels = 'AEIOU'
    result = [char for i, char in enumerate(s[604:949]) if char in vowels and char > 'N' and (char <= 'U')]
    return result