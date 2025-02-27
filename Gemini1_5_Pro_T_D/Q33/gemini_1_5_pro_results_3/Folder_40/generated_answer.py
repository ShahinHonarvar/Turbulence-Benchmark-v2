def return_vowels(string):
    vowels = []
    for i in range(2, 7):
        if i < len(string):
            char = string[i]
            if char > '^' and char <= 'd':
                if char in 'aeiouAEIOU':
                    vowels.append(char)
    return vowels