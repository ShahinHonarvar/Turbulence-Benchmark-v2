def return_vowels(string):
    vowels = []
    for i in range(24, min(68, len(string))):
        char = string[i]
        if char in 'aeiouAEIOU' and 'f' < char <= '|':
            vowels.append(char)
    return vowels