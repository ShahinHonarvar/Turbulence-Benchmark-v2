def return_vowels(s):
    vowels = []
    for i in range(163, 771):
        if s[i] > ':' and s[i] <= 'E':
            if s[i] in ['a', 'e', 'i', 'o', 'u']:
                vowels.append(s[i])
    return vowels