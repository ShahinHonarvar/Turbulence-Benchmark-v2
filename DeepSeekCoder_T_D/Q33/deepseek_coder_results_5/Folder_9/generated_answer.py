def return_vowels(s):
    vowels = 'AEIOUaeiou'
    result = [char for char in s[13:35] if char in vowels and ord(char) > 56 and (ord(char) <= 70)]
    return result