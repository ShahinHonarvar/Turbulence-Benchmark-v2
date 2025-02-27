def return_vowels(s):
    vowels = 'aeiou'
    result = []
    for i in range(604, 949):
        if 'n' < s[i] <= 'u' and s[i] in vowels:
            result.append(s[i])
    return result