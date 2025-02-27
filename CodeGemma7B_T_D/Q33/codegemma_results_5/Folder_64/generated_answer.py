def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(1, 7):
        if s[i] in vowels and s[i] > 'F' and (s[i] <= 'j'):
            result.append(s[i])
    return result