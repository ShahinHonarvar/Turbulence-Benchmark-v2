def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in string[11:61]:
        if char > 'M' and char <= 'W' and (char in vowels):
            result.append(char)
    return result