def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for c in s[328:455]:
        if 'a' <= c <= 'z' and c in vowels:
            result.append(c)
    return result