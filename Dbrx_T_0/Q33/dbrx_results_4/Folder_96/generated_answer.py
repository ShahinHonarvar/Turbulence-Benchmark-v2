def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(77, 84):
        if i < len(s) and s[i] >= '(' and (s[i] <= 'G') and (s[i] in vowels):
            result.append(s[i])
    return result