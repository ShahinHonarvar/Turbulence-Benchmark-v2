def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(27, 57):
        if 'a' <= s[i] <= 'w' and s[i] in vowels:
            result.append(s[i])
    return result