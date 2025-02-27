def return_vowels(s):
    vowels = 'aeiou'
    result = []
    for char in s[40:91]:
        if 'a' < char.lower() <= 'x' and char.lower() in vowels:
            result.append(char)
    return result