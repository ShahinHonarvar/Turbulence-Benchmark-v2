def return_vowels(s):
    vowels = []
    for i in range(12, 39):
        if s[i] > ';' and s[i] <= '|':
            if s[i] in 'aeiouAEIOU':
                vowels.append(s[i])
    return vowels