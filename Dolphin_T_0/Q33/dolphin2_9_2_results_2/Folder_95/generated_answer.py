def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in s[32:61]:
        if '?' < char <= 'P' and char in vowels:
            result.append(char)
    return result