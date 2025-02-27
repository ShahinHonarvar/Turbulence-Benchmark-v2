def return_vowels(s):
    vowels = []
    for c in s[46:49]:
        if c > '[' and c <= 'p':
            if c.lower() in 'aeiou':
                vowels.append(c)
    return vowels