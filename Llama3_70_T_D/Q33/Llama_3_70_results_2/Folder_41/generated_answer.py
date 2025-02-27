def return_vowels(s):
    vowels = []
    for i in range(71, 81):
        if i < len(s):
            char = s[i]
            if (char > '>' and char <= 'U') and char in 'aeiouAEIOU':
                vowels.append(char)
    return vowels