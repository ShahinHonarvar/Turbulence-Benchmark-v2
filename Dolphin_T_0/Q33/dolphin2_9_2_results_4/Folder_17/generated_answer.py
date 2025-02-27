def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    chars = s[60:99]
    result = []
    for c in chars:
        if 'j' < c <= 'n' and c in vowels:
            result.append(c)
    return result