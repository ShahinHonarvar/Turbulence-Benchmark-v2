def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(20, 41):
        if s[i] in vowels and (s[i] > 'k' and s[i] <= 'z'):
            result.append(s[i])
    return result