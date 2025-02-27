def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(20, 41):
        if s[i] > 'K' and s[i] <= 'Z' and (s[i] in vowels):
            result.append(s[i])
    return result