def return_vowels(s):
    vowels = 'AEIOUaeiou'
    result = []
    for i in range(77, 84):
        if i < len(s) and s[i] > '(' and (s[i] <= 'G') and (s[i] in vowels):
            result.append(s[i])
    return result