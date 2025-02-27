def return_vowels(s):
    vowels = 'aeiou'
    desired_chars = s[21:23]
    result = []
    for char in desired_chars:
        if char > ' ' and char <= 'n' and (char in vowels):
            result.append(char)
    return result