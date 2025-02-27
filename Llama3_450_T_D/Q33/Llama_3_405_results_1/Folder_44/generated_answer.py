def return_vowels(s):
    vowels = 'aeiou'
    result = [char for i, char in enumerate(s) if 46 <= i < 49 and '[' < char <= 'p' and (char in vowels)]
    return result