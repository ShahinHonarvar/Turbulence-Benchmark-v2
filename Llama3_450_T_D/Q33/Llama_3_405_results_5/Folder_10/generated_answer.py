def return_vowels(s):
    vowels = 'aeiou'
    result = [char for i, char in enumerate(s[31:37]) if char in vowels and ';' < char <= 't']
    return result