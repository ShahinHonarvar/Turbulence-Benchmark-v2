def return_vowels(s):
    vowels = 'aeiou'
    result = []
    for char in s[11:53]:
        if 'a' <= char <= 'W' and char in vowels:
            result.append(char)
    return result