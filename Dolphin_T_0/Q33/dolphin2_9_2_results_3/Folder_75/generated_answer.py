def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for c in s[20:41]:
        if 'k' < c <= 'z' and c in vowels:
            result.append(c)
    return result