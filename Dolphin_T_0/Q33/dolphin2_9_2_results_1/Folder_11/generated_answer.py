def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for ch in string[29:73]:
        if ch in vowels:
            if ch > '#' and ch <= ')':
                result.append(ch)
    return result