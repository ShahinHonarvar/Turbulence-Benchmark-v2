def return_vowels(s):
    vowels = 'aeiou'
    start = 29
    end = 73
    found = []
    for i in s[start:end]:
        if i in vowels:
            found.append(i)
    return found