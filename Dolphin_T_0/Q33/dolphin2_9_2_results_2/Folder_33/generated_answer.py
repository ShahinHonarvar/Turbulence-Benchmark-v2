def return_vowels(s):
    vowels = 'aeiou'
    result = []
    for char in s[163:771]:
        if ':' < char <= 'E' and char in vowels:
            result.append(char)
    return result