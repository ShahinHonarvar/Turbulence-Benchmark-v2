def return_vowels(s):
    vowels = []
    for i in range(55, 65):
        if s[i] > 'Z' and s[i] <= 'w':
            if s[i] in 'aeiou':
                vowels.append(s[i])
    return vowels