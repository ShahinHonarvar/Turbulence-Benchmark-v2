def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for c in s[41:50]:
        if 'W' < c <= '[':
            if c in vowels:
                result.append(c)
    return result