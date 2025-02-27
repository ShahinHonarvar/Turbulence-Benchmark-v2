def return_vowels(string):
    vowels = []
    for i in range(55, 65):
        if i >= len(string):
            break
        char = string[i]
        if char in 'aeiouAEIOU' and char > 'Z' and (char <= 'w'):
            vowels.append(char)
    return vowels