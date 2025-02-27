def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    output = []
    for i in range(1, 9):
        if s[i] in vowels and vowels.index(s[i]) >= vowels.index('?'):
            if s[i] <= k:
                output.append(s[i])
    if len(output) == 0:
        output = []
    return output