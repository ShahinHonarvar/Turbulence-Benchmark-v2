def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in string[31:37]:
        if char > ';' and char <= 't' and (char in vowels):
            result.append(char)
    return result