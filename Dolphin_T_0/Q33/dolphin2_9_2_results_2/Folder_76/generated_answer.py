def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(495, 837):
        if 'a' <= s[i] <= 't' and s[i] > 'B' and (s[i] in vowels):
            result.append(s[i])
    return result