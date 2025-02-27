def return_vowels(s):
    vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(11, 61):
        if 'M' < s[i] <= 'W' and s[i] in vowels:
            result.append(s[i])
    return result