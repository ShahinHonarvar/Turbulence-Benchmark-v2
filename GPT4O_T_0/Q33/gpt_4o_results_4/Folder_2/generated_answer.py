def return_vowels(s):
    vowels = 'AEIOUaeiou'
    return [char for char in s[170:645] if char in vowels and 'E' < char <= '~']