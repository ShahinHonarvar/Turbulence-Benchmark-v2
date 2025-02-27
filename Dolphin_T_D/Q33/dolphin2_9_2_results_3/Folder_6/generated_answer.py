def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(20, 34):
        if 'u' < s[i] <= 'i':
            if s[i] in vowels:
                result.append(s[i])
    return result