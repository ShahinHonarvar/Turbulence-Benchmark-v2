def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(19, 32):
        if s[i] > '0' and s[i] <= '7':
            return_vowels.append([s[i] for s[i] in vowels if s[i] > '0' and s[i] <= '7'])
    return result