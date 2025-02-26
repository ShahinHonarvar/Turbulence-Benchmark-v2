def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = []
    for i in range(23, 57):
        if i < len(s) and s[i] in vowels and ('0' < s[i] <= 'd'):
            result.append(s[i])
    return result