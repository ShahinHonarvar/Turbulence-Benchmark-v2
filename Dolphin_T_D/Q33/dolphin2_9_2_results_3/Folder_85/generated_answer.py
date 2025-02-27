def return_vowels(s):
    accepted_chars = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(55, 65):
        if s[i] > 'Z' and s[i] <= 'w':
            if s[i] in accepted_chars:
                result.append(s[i])
    return result