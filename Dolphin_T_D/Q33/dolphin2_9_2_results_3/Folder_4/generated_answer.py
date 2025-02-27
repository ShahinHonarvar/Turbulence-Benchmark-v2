def return_vowels(s):
    vowels = 'aeiou'
    if s[40:91] == '':
        return []
    else:
        returned = []
        for char in s[40:91]:
            if 'a' < char.lower() <= 'x' and char.lower() in vowels:
                returned.append(char)
    return returned