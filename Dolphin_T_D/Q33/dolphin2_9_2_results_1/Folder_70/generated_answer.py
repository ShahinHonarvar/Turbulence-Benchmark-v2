def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for c in s[171:402]:
        if 'i' < c <= 'k' and c in vowels:
            result.append(c)
    return result