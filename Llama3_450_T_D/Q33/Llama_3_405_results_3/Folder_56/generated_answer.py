def return_vowels(s):
    vowels = 'AEIOUaeiou'
    return [char for char in s[15:86] if char in vowels and '@' < char <= '~']