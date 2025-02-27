def return_vowels(s):
    vowels = 'aeiou'
    result = []
    for char in s[14:60]:
        if 'D' < char <= 'v' and char in vowels:
            result.append(char)
    return result