def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in s[47:61]:
        if char > '9' and char <= 'O' and (char in vowels):
            result.append(char)
    return result