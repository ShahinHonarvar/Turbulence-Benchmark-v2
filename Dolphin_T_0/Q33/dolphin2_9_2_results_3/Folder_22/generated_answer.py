def return_vowels(s):
    vowels = []
    for i in range(56, 90):
        char = s[i]
        if 'K' < char <= 'z' and char in 'aeiou':
            vowels.append(char)
    return vowels