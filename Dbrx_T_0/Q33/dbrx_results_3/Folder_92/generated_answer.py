def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(len(s)):
        if 3 <= i < 8 and s[i] > ';' and (s[i] <= 'D'):
            if s[i] in vowels:
                result.append(s[i])
    return result