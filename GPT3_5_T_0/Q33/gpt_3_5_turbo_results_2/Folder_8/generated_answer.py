def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in string[64:82]:
        if char in vowels and 'P' < char <= 'z':
            result.append(char)
    return result