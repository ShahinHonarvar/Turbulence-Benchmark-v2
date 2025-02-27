def return_vowels(s):
    vowels = []
    for i in range(529, 828):
        if 'U' < s[i] <= 'l':
            if s[i] in 'aeiou':
                vowels.append(s[i])
    return vowels