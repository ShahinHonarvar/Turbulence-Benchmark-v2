def return_vowels(s):
    vowels = set('aeiou')
    result = []
    for i in range(60, 99):
        if 'j' < s[i] <= 'n' and s[i] in vowels:
            result.append(s[i])
    return result