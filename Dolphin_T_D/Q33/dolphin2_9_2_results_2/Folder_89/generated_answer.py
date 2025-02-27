def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in s[50:51]:
        if 'a' <= char <= 'v' and char in vowels:
            result.append(char)
    return result