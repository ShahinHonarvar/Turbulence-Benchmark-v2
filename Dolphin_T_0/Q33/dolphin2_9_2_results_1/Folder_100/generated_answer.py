def return_vowels(s):
    vowels = []
    for i in range(23, 75):
        if 'L' < s[i] <= 'd':
            if s[i] in 'aeiou':
                vowels.append(s[i])
    return vowels