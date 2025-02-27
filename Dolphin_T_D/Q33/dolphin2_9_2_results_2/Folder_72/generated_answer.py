def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(37, 57):
        if s[i] > '*' and s[i] <= 'P':
            if s[i] in vowels:
                result.append(s[i])
    return result