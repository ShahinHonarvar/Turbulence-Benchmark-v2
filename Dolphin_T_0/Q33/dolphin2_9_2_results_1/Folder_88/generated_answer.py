def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(70, 76):
        if 'a' <= s[i] <= ':' and s[i] in vowels and (s[i] > '2'):
            result.append(s[i])
    return result