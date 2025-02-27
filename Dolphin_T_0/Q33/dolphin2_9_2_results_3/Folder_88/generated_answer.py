def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for c in s[70:76]:
        if c in vowels and ord('2') < ord(c) <= ord(':'):
            result.append(c)
    return result