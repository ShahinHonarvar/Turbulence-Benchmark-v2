def return_vowels(s):
    vowels = 'AEIOUaeiou'
    result = []
    for i in range(40, 91):
        if i < len(s) and s[i] in vowels and ('A' < s[i] <= 'x'):
            result.append(s[i])
    return result