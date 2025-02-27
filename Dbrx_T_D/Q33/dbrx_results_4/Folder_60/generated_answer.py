def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in s[24:59]:
        if 'n' < char <= 'u' and char in vowels:
            result.append(char)
    return result