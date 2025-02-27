def return_vowels(s):
    vowels = 'aeiou'
    result = []
    for i in range(529, 828):
        if 'U' < s[i] <= 'l' and s[i] in vowels:
            result.append(s[i])
    return result