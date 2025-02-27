def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(77, 84):
        if '(' < s[i] <= 'G':
            if s[i] in vowels:
                result.append(s[i])
    return result