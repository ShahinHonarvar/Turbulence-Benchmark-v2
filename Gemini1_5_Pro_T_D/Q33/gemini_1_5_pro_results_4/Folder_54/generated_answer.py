def return_vowels(string):
    vowels = []
    for i in range(23, 85):
        if i < len(string):
            char = string[i]
            if char in 'aeiouAEIOU' and char > 'W' and (char <= 'v'):
                vowels.append(char)
    return vowels