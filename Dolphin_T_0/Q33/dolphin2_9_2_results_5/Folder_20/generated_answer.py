def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in s[59:61]:
        if '+' < char <= 'h' and char in vowels:
            result.append(char)
    return result