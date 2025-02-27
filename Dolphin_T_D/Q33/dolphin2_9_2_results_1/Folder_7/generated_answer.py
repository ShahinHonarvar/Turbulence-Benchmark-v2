def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for c in s[202:872]:
        if c in vowels and ord(c) > 3 and (ord(c) <= ord('>')):
            result.append(c)
    return result