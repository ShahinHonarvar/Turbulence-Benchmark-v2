def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for c in s[837:975]:
        if vowels.__contains__(c.lower()) and c > 'n' and (c <= 'w'):
            result.append(c)
    return result