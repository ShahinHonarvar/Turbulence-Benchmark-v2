def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(len(s)):
        if 323 <= i < 526 and s[i] > '+' and (s[i] <= ':'):
            if s[i] in vowels:
                result.append(s[i])
    return result