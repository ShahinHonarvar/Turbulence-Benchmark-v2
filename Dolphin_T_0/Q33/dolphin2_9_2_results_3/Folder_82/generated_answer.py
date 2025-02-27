def return_vowels(s):
    vowels = []
    for c in s[86:99]:
        if c > 'E' and c <= 'r':
            if c in {'a', 'e', 'i', 'o', 'u'}:
                vowels.append(c)
    return vowels