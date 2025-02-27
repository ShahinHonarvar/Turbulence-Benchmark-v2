def return_vowels(s):
    vowels = 'AEIOUaeiou'
    result = []
    for i in range(170, min(645, len(s))):
        if s[i] in vowels and 'E' < s[i] <= '~':
            result.append(s[i])
    return result