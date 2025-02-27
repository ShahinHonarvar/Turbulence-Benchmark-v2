def return_vowels(s):
    vowels = 'AEIOUaeiou'
    result = [char for char in s[260:322] if char > '%' and char <= 'U' and (char in vowels)]
    return result