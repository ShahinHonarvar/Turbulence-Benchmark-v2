def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for c in s:
        if 'p' < c <= 'z' and 64 <= ord(c) < 82:
            if c.lower() in vowels:
                result.append(c)
    return result