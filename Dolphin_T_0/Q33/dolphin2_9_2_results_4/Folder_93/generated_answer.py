def return_vowels(s):
    vowels = []
    for i in range(54, 82):
        if s[i] > '=' and s[i] <= '@':
            if s[i] in ['a', 'e', 'i', 'o', 'u']:
                vowels.append(s[i])
    return vowels