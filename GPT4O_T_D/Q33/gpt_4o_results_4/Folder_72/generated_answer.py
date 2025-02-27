def return_vowels(s):
    vowels = 'AEIOUaeiou'
    result = []
    for i in range(37, min(57, len(s))):
        if s[i] in vowels and '*' < s[i] <= 'P':
            result.append(s[i])
    return result