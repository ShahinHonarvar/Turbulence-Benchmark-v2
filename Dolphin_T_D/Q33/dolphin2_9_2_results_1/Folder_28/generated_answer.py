def return_vowels(s):
    vowels = 'aeiou'
    result = [s[i] for i in range(41, 50) if s[i] in vowels and 'W' < s[i] <= '[']
    return result