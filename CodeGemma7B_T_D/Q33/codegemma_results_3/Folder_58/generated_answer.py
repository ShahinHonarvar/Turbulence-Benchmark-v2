def return_vowels(s):
    vowels = []
    for i in range(260, 322):
        if s[i] in '%U' and s[i].lower() in 'aeiou':
            vowels.append(s[i])
    return vowels