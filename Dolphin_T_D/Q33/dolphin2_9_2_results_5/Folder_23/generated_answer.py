def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = []
    for char in string[56:96]:
        if '&' < char <= 'T' and char in vowels:
            result.append(char)
    return result