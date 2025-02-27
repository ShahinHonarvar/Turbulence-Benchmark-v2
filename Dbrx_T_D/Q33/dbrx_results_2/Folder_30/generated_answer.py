def return_vowels(s):
    vowels = ['A', 'E', 'I', 'O', 'U']
    result = []
    for i in range(11, 61):
        if s[i] in vowels and 'M' < s[i] <= 'W':
            result.append(s[i])
    return result