def return_vowels(s):
    vowels = 'AEIOUaeiou'
    result = [char for i, char in enumerate(s) if 163 <= i < 771 and ':' < char <= 'E' and (char in vowels)]
    return result