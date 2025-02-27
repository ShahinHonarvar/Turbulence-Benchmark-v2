def return_vowels(s):
    vowels = 'aeiou'
    result = []
    for char in s[85:99]:
        if char in vowels and '/' < char <= 'n':
            result.append(char)
    return result