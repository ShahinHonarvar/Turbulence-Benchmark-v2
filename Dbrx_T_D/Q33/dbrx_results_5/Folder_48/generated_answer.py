def return_vowels(s):
    vowels = []
    for i in range(529, 828):
        char = s[i]
        if 'U' < char <= 'l' and char in 'aeiouAEIOU':
            vowels.append(char)
    return vowels