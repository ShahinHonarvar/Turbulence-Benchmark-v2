def return_vowels(s):
    vowels = 'aeiou'
    result = []
    for char in s[770:852]:
        if 'B' < char <= 'i' and char in vowels:
            result.append(char)
    return result