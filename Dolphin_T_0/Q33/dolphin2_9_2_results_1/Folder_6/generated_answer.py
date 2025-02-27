def return_vowels(s):
    vowels = 'aeiou'
    result = []
    for ch in s[20:34]:
        if 'U' < ch <= 'i':
            if ch in vowels:
                result.append(ch)
    return result