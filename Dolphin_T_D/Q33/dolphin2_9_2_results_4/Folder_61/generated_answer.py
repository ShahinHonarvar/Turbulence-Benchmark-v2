def return_vowels(s):
    vowels = []
    for i in range(1, 4):
        if s[i] in 'aeiou':
            if s[i] > 'c' and s[i] <= 'i':
                vowels.append(s[i])
    return vowels