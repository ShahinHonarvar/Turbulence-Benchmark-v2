def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    found = []
    for i in range(36, 56):
        if s[i] > '+' and s[i] <= '/' and (s[i] in vowels):
            found.append(s[i])
    return found