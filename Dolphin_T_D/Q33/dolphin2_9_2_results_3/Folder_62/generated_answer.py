def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    output = []
    for c in s[14:60]:
        if c > 'D' and c <= 'v':
            if c in vowels:
                output.append(c)
    return output