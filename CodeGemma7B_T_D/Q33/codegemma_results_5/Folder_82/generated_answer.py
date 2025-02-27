def return_vowels(s):
    vowels = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
    result = []
    for i in range(86, 99):
        if s[i] in vowels and s[i] > 'E' and (s[i] <= 'r'):
            result.append(s[i])
    return result