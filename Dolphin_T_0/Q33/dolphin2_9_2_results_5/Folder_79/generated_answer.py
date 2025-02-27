def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in s[74:96]:
        if 'I' < char <= 'X' and char in vowels:
            result.append(char)
    return result