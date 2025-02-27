def return_vowels(s):
    vowels = 'aeiou'
    result = []
    for char in s[17:65]:
        if char > 'U' and char <= '{' and (char.lower() in vowels):
            result.append(char)
    return result