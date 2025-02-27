def return_vowels(s):
    vowels = 'aeiou'
    result = [char for char in s[50:51] if char in vowels and ',' < char <= 'v']
    return result