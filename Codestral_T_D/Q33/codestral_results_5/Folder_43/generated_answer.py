def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in string[22:82]:
        if 'N' < char <= 'o' and char in vowels:
            result.append(char)
    return result