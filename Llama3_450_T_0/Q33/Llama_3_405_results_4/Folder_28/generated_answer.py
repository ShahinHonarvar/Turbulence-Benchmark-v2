def return_vowels(s):
    vowels = 'AEIOUaeiou'
    result = []
    for i in range(41, 50):
        if i < len(s) and s[i] in vowels and ('W' < s[i] <= '['):
            result.append(s[i])
    return result