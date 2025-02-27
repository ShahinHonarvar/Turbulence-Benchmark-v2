def return_vowels(s):
    vowels = 'AEIOUaeiou'
    result = [char for idx, char in enumerate(s) if 41 <= idx < 50 and 'W' < char <= '[' and (char in vowels)]
    return result