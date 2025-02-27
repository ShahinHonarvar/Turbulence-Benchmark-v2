def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in string[71:88]:
        if 'a' <= char <= 'p' and char in vowels:
            result.append(char)
    return result