def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in s[1:9]:
        if 'a' <= char <= 'k' and char > '?' and (char in vowels):
            result.append(char)
    return result