def return_vowels(string):
    vowels = 'aeiou'
    result = []
    for ch in string[74:96]:
        if ch > 'I' and ch <= 'X' and (ch in vowels):
            result.append(ch)
    return result