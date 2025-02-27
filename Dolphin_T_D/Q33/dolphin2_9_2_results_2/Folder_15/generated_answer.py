def return_vowels(s):
    vowels = []
    for char in s[5:6]:
        if char > '3' and char <= '^':
            if char in 'aeiouAEIOU':
                vowels.append(char)
    return vowels