def return_vowels(s):
    vowels = 'aeiou'
    result = []
    for i in range(20, 43):
        if 5 < ord(s[i].lower()) <= ord('m'):
            if s[i].lower() in vowels:
                result.append(s[i])
    return result