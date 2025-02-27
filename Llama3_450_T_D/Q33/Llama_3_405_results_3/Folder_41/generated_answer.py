def return_vowels(s):
    vowels = 'AEIOU'
    return [char for i, char in enumerate(s[71:81]) if char in vowels and '>' < char <= 'U']