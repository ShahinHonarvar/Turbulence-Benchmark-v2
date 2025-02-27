def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in s[44:95]:
        if 'a' <= char <= 'z' and char in vowels:
            result.append(char)
    return result