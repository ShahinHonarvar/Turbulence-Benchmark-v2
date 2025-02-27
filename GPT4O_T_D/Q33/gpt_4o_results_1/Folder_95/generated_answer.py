def return_vowels(s):
    vowels = 'AEIOUaeiou'
    result = []
    for char in s[32:61]:
        if '>' < char <= 'P' and char in vowels:
            result.append(char)
    return result