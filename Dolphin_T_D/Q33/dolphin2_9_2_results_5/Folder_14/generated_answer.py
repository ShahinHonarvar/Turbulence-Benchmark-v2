def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = []
    for c in s[47:61]:
        if c > '9' and c <= 'O' and (c in vowels):
            result.append(c)
    return result