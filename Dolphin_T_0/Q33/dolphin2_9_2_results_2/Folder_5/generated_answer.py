def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for c in s[44:95]:
        if c > '>' and c <= '<':
            if c in vowels:
                result.append(c)
    return result