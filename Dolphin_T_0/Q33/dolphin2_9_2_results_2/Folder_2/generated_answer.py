def return_vowels(s):
    vowels = []
    for char in s[170:645]:
        if char > 'E' and char <= '~':
            vowels.append(char)
    return vowels