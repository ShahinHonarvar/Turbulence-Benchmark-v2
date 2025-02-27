def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(770, 852):
        if s[i] in vowels and s[i] > 'B' and (s[i] <= 'i'):
            result.append(s[i])
    return result