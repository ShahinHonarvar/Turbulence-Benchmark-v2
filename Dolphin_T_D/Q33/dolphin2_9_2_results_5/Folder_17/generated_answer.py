def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(60, 99):
        if s[i] > 'j' and s[i] <= 'n':
            if s[i] in vowels:
                result.append(s[i])
    return result