def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in s[5:6]:
        if 'a' <= char <= '^' and char in vowels and (char > '3'):
            result.append(char)
    return result