def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(260, 322):
        if s[i] > '%' and s[i] <= 'U':
            if s[i] in vowels:
                result.append(s[i])
    return result