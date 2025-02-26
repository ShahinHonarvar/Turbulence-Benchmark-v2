def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = []
    for char in string[54:82]:
        if char in vowels and '=' < char <= '@':
            result.append(char)
    return result