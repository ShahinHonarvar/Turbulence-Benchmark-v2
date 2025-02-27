def return_vowels(s):
    vowels = 'aeiou'
    result = [char for i, char in enumerate(s[34:58]) if char in vowels and 'b' < char <= 'o']
    return result