def return_vowels(s):
    vowels = 'aeiou'
    result = [s[i] for i in range(34, 58) if 'b' < s[i] <= 'o' and s[i] in vowels]
    return result