def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(20, 34):
        if i < len(s) and s[i] in vowels and ('U' < s[i] <= 'i'):
            result.append(s[i])
    return result