def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    results = []
    for i in range(77, 84):
        if '(' < s[i] <= 'G':
            for v in vowels:
                if s[i] == v:
                    results.append(s[i])
    return results