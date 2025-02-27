def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(len(s)):
        if i >= 90 and i < 97:
            if s[i] > '_' and s[i] <= 'x' and (s[i] in vowels):
                result.append(s[i])
    return result