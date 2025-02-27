def return_vowels(s):
    vowels = []
    for i in range(1, 5):
        if i < len(s):
            c = s[i]
            if '!' < c <= 'j' and c.lower() in 'aeiou':
                vowels.append(c)
    return vowels