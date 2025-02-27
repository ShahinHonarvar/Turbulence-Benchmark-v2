def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in string[328:455]:
        if 'a' <= char <= 'z' and char in vowels:
            result.append(char)
    return result