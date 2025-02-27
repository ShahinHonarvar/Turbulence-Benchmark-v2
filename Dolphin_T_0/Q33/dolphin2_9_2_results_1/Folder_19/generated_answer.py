def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(51, 77):
        if 4 < ord(s[i]) <= ord('='):
            if s[i] in vowels:
                result.append(s[i])
    return result