def return_vowels(s):
    vowels = 'aeiou'
    result = [char for i, char in enumerate(s[29:73]) if char in vowels and '#' < char <= '.']
    return result