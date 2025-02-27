def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(20, 43):
        if 5 < ord(s[i]) <= ord('M') and s[i] in vowels:
            result.append(s[i])
    return result