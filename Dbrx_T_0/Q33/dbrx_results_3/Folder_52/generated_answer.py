def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(len(s)):
        if 24 <= i < 68 and s[i] > 'f' and (s[i] <= '|'):
            if s[i] in vowels:
                result.append(s[i])
    return result