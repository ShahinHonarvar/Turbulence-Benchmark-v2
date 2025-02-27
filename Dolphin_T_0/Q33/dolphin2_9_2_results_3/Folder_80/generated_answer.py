def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    output = []
    for c in s[85:99]:
        if '/' < c <= 'n' and c in vowels:
            output.append(c)
    return output