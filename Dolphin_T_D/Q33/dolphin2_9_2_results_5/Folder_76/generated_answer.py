def return_vowels(s):
    vowels = []
    for i in range(495, 837):
        if 'B' < s[i] <= 't':
            if s[i] in 'aeiou':
                vowels.append(s[i])
    return vowels