def return_vowels(s):
    vowels = 'aeiou'
    result = [s[i] for i in range(23, 57) if s[i] in vowels and 'a' <= s[i] <= 'd']
    return result