def return_vowels(s):
    vowels_list = []
    vowels = 'aeiou'
    for i in range(483, 664):
        if '\\' < s[i] <= 'h' and s[i] in vowels:
            vowels_list.append(s[i])
    return vowels_list