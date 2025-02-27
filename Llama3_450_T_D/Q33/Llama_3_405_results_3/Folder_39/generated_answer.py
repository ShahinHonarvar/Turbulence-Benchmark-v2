def return_vowels(s):
    vowels = 'AEIOUaeiou'
    result = []
    for c in s:
        if 32 <= ord(c) < 97 and c > 'Q' and (c <= ']') and (c in vowels):
            result.append(c)
    return result