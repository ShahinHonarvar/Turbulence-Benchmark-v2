def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(len(s)):
        if 2 <= i < 7 and s[i] > '^' and (s[i] <= 'd') and (s[i] in vowels):
            result.append(s[i])
    return result