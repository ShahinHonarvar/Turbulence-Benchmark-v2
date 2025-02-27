def return_vowels(s):
    vowels = 'AEIOUaeiou'
    return [char for char in s[171:402] if char in vowels and 'I' < char <= 'k']