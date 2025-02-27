def return_vowels(s):
    vowels = 'aeiou'
    result = []
    for char in s[47:89]:
        if char.lower() in vowels and '@' < char <= 'n':
            result.append(char)
    return result