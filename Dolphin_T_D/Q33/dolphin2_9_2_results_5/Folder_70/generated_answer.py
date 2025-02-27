def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    char_range = s[171:402]
    result = []
    for char in char_range:
        if 'i' < char <= 'k' and char.lower() in vowels:
            result.append(char)
    return result