def return_vowels(s):
    vowels = 'aeiou'
    output = []
    for char in s[23:57]:
        if 'a' <= char <= 'd' and char > '0' and (char in vowels):
            output.append(char)
    return output