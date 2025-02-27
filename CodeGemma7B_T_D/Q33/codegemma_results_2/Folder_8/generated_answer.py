def return_vowels(str):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in str[64:82]:
        if char in vowels and char > 'P' and (char <= 'z'):
            result.append(char)
    return result