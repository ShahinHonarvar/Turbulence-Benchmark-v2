def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    char_list = list(s[8:9])
    result = []
    for char in char_list:
        if char in vowels and char > 'Y' and (char <= 's'):
            result.append(char)
    return result