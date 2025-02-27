def return_vowels(s):
    vowels = 'aeiou'
    result = []
    for char in s[1:9]:
        if char in vowels and '?' < char <= 'k':
            result.append(char)
    return result