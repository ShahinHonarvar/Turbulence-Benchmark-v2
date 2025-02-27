def return_vowels(l):
    result = []
    a = ord('a')
    z = ord('z')
    for i in range(36, 56):
        c = chr(a + i)
        if c.lower() in l and c <= '/' and (c > '+'):
            result.append(c)
    return result