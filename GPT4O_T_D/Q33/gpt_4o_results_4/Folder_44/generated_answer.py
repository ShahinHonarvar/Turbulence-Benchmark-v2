def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = []
    for c in s[46:49]:
        if c in vowels and '[' < c <= 'p':
            result.append(c)
    return result