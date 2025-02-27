def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(len(s)):
        if s[i] >= 'E' and s[i] <= 'r' and (i >= 86) and (i < 99) and (s[i] in vowels):
            result.append(s[i])
    return result