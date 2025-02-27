def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = []
    for i in range(15, 86):
        if '@' < s[i] <= '~':
            if s[i] in vowels:
                result.append(s[i])
    return result