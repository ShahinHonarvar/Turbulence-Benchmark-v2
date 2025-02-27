def return_vowels(s):
    result = []
    vowels = ['a', 'e', 'i', 'o', 'u']
    for char in s[74:96]:
        if 'I' < char <= 'X' and char.lower() in vowels:
            result.append(char)
    return result