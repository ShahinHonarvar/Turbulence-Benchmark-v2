def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(641, 872):
        if i < len(s):
            if s[i] > '>' and s[i] <= 'q':
                if s[i] in vowels:
                    result.append(s[i])
    return result