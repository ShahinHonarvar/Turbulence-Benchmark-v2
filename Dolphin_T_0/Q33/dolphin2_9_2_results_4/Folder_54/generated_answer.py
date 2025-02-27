def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(23, 85):
        if i < 23 or i >= 85:
            continue
        if s[i] in vowels and s[i] > 'W' and (s[i] <= 'v'):
            result.append(s[i])
    return result