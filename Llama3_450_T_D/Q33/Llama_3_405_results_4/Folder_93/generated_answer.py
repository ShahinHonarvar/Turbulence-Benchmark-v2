def return_vowels(s):
    vowels = 'AEIOUaeiou'
    result = []
    for i in range(54, min(82, len(s))):
        if s[i] in vowels and '=' < s[i] <= '@':
            result.append(s[i])
    return result