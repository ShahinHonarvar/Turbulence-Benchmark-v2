def return_vowels(s):
    result = []
    vowels = ['a', 'e', 'i', 'o', 'u']
    for char in s[31:37]:
        if ';' < char <= 't' and char in vowels:
            result.append(char)
    return result