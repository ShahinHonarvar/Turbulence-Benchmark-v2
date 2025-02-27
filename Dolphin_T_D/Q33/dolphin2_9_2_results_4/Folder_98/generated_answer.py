def return_vowels(s):
    vowels = ['A', 'E', 'I', 'O', 'U']
    result = []
    for c in s[3:9]:
        if c in vowels and c > 'S' and (c <= 'U'):
            result.append(c)
    return result