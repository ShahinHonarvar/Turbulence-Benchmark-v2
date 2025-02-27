def return_vowels(s):
    vowels = []
    for i in range(17, 65):
        if 'U' < s[i] <= '{' and s[i] in 'aeiouAEIOU':
            vowels.append(s[i])
    return vowels