def return_vowels(s):
    vowels = 'AEIOUaeiou'
    result = [char for i, char in enumerate(s) if 17 <= i < 65 and 'U' < char <= '{' and (char in vowels)]
    return result