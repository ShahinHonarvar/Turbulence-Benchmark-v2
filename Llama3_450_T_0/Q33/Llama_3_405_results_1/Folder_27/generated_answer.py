def return_vowels(s):
    vowels = 'aeiou'
    result = [char for i, char in enumerate(s) if 29 <= i < 31 and 'a' < char <= 'f' and (char in vowels)]
    return result