def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in s[19:32]:
        if 'a' <= char <= 'u' and char in vowels:
            result.append(char)
    return result