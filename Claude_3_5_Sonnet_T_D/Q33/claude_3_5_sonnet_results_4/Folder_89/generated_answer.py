def return_vowels(s):
    vowels = 'aeiou'
    result = []
    if len(s) > 50:
        for char in s[50:51]:
            if char in vowels and ',' < char <= 'v':
                result.append(char)
    return result