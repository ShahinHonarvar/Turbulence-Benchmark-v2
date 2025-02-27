def return_vowels(s):
    vowels = ''
    for i in range(50, 77):
        if s[i] > '#' and s[i] <= 'r':
            vowels += s[i]
    return [vowels] if vowels else []