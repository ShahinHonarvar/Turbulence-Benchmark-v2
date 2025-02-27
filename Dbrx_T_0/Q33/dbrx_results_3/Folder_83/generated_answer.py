def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(len(s)):
        if 90 <= i < 97 and s[i] > '_' and (s[i] <= 'x') and (s[i] in vowels):
            result.append(s[i])
    return result