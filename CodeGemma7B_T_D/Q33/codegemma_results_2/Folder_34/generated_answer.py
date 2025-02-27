def return_vowels(strg):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = []
    for _ in range(19, 32):
        if _ in vowels and ord(strg[_]) > ord(0) and (ord(strg[_]) <= ord(7)):
            result.append(strg[_])
    return result