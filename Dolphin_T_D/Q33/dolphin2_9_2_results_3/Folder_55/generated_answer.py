def return_vowels(s):
    vowels = []
    for i in range(1, 5):
        if s[i] > '!' and s[i] <= 'j':
            if s[i] in 'aeiou':
                vowels.append(s[i])
    return vowels