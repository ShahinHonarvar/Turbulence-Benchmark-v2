def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for c in s[12:39]:
        if ';' < c <= '|':
            if c in vowels:
                result.append(c)
    return result