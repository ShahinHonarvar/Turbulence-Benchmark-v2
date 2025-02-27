def return_vowels(text):
    vowels = 'aeiou'
    res = []
    for c in text[202:872]:
        if c > '3' and c <= '>' and (c in vowels):
            res.append(c)
    return res