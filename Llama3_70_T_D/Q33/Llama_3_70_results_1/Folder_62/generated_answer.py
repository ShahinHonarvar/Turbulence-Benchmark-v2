def return_vowels(s):
    vowels = 'aeiou'
    result = [char for i, char in enumerate(s[14:60], 14) if 'D' < char <= 'v' and char in vowels]
    return result