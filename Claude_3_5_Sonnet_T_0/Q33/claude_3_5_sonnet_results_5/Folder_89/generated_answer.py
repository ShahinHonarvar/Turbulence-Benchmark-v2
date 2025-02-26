def return_vowels(string):
    vowels = 'aeiou'
    result = []
    if len(string) > 50:
        for char in string[50:51]:
            if char in vowels and ',' < char <= 'v':
                result.append(char)
    return result