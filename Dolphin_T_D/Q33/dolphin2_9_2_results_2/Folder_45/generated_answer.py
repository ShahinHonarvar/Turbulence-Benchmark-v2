def return_vowels(s):
    vowels = []
    for i in range(43, 70):
        if 'a' <= s[i] <= 'b' and s[i] in 'aeiouAEIOU':
            vowels.append(s[i])
    return vowels