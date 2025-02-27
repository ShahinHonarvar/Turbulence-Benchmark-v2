def return_vowels(s):
    vowels = []
    for i in range(54, 82):
        char = s[i]
        if 'e' <= char <= 'i' and i in range(54, 82):
            vowels.append(char)
    return vowels