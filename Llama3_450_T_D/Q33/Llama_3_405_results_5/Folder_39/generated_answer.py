def return_vowels(s):
    vowels = 'AEIOUaeiou'
    result = [char for char in s if 32 <= ord(char) < 97 and 'Q' < char <= ']' and (char in vowels)]
    return result