def return_vowels(s):
    vowels = 'aeiou'
    result = []
    for char in s[90:97]:
        if vowels.find(char) != -1 and char > '_' and (char <= 'x'):
            result.append(char)
    return result