def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(44, 95):
        if '5' < s[i] <= '<':
            if s[i] in vowels:
                result.append(s[i])
    return result