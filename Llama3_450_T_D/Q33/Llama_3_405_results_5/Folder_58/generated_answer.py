def return_vowels(s):
    vowels = 'AEIOU'
    result = []
    for i in range(260, 322):
        if i < len(s) and s[i] > '%' and (s[i] <= 'U') and (s[i] in vowels):
            result.append(s[i])
    return result