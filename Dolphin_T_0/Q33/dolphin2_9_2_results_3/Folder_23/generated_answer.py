def return_vowels(s):
    vowels = 'aeiou'
    result = [s[i] for i in range(56, 96) if i < len(s) and s[i] > '&' and (s[i] <= 'T') and (s[i] in vowels)]
    return result