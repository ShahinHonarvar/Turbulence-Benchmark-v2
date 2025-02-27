def return_vowels(s):
    vowels = 'AEIOUaeiou'
    result = []
    for char in s:
        if 32 <= ord(char) < 97 and ord(char) > ord('Q') and (ord(char) <= ord(']')) and (char in vowels):
            result.append(char)
    return result