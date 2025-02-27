def return_vowels(s):
    vowels = ['A', 'E', 'I', 'O', 'U']
    result = []
    for i in range(56, 68):
        if 'M' < s[i] <= 'X' and s[i] in vowels:
            result.append(s[i])
    return result