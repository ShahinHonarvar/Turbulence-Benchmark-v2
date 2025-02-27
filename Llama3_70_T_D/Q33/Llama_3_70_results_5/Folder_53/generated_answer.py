def return_vowels(s):
    vowels = []
    for i in range(27, 57):
        if i < len(s):
            char = s[i]
            if 'o' < char <= 'w' and char in 'aeiou':
                vowels.append(char)
    return vowels