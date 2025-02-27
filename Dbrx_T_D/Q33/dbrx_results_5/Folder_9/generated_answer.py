def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in s[13:35]:
        if '8' <= char <= 'F' and char.lower() in vowels:
            result.append(char)
    return result