def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(10, 97):
        if len(s) > i and s[i] >= 'R' and (s[i] <= 'b') and (s[i] in vowels):
            result.append(s[i])
    return result