def return_vowels(s):
    vowels = []
    for i in range(41, 50):
        if i < len(s):
            char = s[i]
            if char > 'W' and char <= '[' and (char in 'AEIOU'):
                vowels.append(char)
    return vowels