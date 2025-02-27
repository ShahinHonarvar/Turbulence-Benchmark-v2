def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(29, 73):
        if s[i] in vowels and s[i] > '#' and (s[i] <= '('):
            result.append(s[i])
    return result