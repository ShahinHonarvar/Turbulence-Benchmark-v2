def return_vowels(string):
    vowels = []
    for char in string[50:77]:
        if char in ['a', 'e', 'i', 'o', 'u'] and char > '#' and (char <= 'r'):
            vowels.append(char)
    return vowels