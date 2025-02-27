def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in string[56:90]:
        if 'K' < char <= 'z' and char in vowels:
            result.append(char)
    return result