def return_vowels(s):
    vowels = []
    for i in range(31, 37):
        if s[i] > ';' and s[i] <= 't':
            if s[i] in 'aeiouy':
                vowels.append(s[i])
    return vowels