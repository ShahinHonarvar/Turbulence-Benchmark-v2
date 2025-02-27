def return_vowels(s):
    vowels = 'AEIOUaeiou'
    result = []
    for i in range(163, min(771, len(s))):
        if s[i] in vowels and ':' < s[i] <= 'E':
            result.append(s[i])
    return result