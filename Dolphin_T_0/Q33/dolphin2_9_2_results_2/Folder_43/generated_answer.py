def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    if len(s) >= 82:
        for i in range(22, 82):
            if s[i] > 'n' and s[i] <= 'o':
                if s[i] in vowels:
                    result.append(s[i])
    return result