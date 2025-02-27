def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(45, 76):
        if 'b' < s[i] <= 'z' and s[i] in vowels:
            result.append(s[i])
    return result