def return_vowels(string):
    vowels = 'aeiou'
    result = [c for c in string[50:77] if c > '#' and c <= 'r' and (c in vowels)]
    return result