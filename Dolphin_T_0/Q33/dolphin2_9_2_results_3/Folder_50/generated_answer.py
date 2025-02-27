def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in s[11:53]:
        if 'a' <= char <= 'W':
            if char in vowels:
                result.append(char)
    return result