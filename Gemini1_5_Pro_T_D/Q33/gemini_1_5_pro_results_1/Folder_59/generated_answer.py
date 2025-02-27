def return_vowels(string):
    vowels = []
    for i in range(8, 9):
        if i < len(string):
            char = string[i]
            if char > 'Y' and char <= 's' and (char in 'aeiouAEIOU'):
                vowels.append(char)
    return vowels