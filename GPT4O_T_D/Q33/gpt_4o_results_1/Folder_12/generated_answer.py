def return_vowels(s):
    vowels = 'aeiou'
    result = []
    for char in s[13:37]:
        if char in vowels and 'Z' < char <= '}':
            result.append(char)
    return result