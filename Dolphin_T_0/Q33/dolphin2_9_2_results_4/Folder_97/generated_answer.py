def return_vowels(string):
    vowels = 'aeiou'
    result = []
    for ch in string[328:455]:
        if 'a' <= ch <= 'z' and ch in vowels:
            result.append(ch)
    return result