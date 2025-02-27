def return_vowels(s):
    result = []
    for i in range(55, 65):
        if 'Z' < s[i] <= 'w' and s[i] in 'aeiou':
            result.append(s[i])
    return result