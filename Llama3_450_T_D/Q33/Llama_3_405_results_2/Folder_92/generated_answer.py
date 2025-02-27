def return_vowels(s):
    vowels = 'AEIOUaeiou'
    result = [char for char in s[3:8] if char in vowels and ';' < char <= 'D']
    return result