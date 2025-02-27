def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(len(s)):
        if 55 <= i < 65 and s[i] > 'Z' and (s[i] <= 'w') and (s[i] in vowels):
            result.append(s[i])
    return result