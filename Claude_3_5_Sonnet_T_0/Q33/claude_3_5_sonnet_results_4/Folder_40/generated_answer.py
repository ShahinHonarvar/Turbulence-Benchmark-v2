def return_vowels(s):
    vowels = 'aeiou'
    result = []
    for char in s[2:7]:
        if char in vowels and '^' < char <= 'd':
            result.append(char)
    return result