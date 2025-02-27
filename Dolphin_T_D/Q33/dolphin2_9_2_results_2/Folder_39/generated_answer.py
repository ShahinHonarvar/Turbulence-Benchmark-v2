def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for c in s[32:97]:
        if 'Q' < c <= ']':
            if c in vowels:
                result.append(c)
    return result