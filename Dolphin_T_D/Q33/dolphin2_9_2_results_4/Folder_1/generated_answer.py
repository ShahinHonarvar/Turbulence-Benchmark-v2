def return_vowels(s):
    vowels = 'aeiou'
    result = []
    s = s[24:64]
    for char in s:
        if 'F' < char <= 'h':
            if char in vowels:
                result.append(char)
    return result