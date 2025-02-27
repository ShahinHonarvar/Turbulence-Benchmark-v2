def return_vowels(s):
    vowels = []
    for i in s[21:23]:
        if i > 'a' and i <= 'n':
            if i.lower() in ['a', 'e', 'i', 'o', 'u']:
                vowels.append(i)
    return vowels