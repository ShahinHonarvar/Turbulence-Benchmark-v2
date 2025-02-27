def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(43, 70):
        if '*' < s[i] <= 'b' and s[i] in vowels:
            result.append(s[i])
    return result