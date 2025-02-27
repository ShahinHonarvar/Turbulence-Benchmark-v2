def return_vowels(string):
    vowels = []
    for i in range(13, 35):
        char = string[i]
        if char.lower() in ['a', 'e', 'i', 'o', 'u'] and 8 < ord(char) <= 15:
            vowels.append(char)
    return vowels