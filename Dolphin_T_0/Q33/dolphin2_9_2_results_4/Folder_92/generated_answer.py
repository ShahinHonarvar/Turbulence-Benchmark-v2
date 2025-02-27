def return_vowels(s):
    result = []
    vowels = 'aeiou'
    for char in s[3:8]:
        if ';' < char <= 'D':
            if char in vowels:
                result.append(char)
    return result