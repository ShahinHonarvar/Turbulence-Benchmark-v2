def return_vowels(s):
    vowels = 'AEIOUaeiou'
    result = []
    for char in s[12:39]:
        if char > ';' and char <= '|' and (char in vowels):
            result.append(char)
    return result