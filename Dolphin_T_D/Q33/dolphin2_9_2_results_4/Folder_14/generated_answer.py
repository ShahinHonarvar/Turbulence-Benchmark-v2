def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = []
    for i in range(47, 61):
        if s[i] in vowels:
            if s[i] > '9' and s[i] <= 'O':
                result.append(s[i])
    return result