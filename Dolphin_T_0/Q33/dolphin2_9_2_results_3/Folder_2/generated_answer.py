def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    chars = []
    for i in range(170, 645):
        for v in vowels:
            if s[i] == v and s[i] > 'E' and (s[i] <= '~'):
                chars.append(s[i])
    return chars