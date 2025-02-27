def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(37, 57):
        if i >= len(s):
            break
        if s[i] > '*' and s[i] <= 'P' and (s[i] in vowels):
            result.append(s[i])
    return result