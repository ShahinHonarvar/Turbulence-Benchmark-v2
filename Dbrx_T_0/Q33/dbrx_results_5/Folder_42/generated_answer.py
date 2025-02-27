def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(12, 39):
        if s[i] > ';' and s[i] <= '|':
            if s[i] in vowels:
                result.append(s[i])
    return result