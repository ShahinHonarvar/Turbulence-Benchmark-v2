def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    substring = string[44:95]
    for char in substring:
        if char in vowels and char > '5' and (char <= '<'):
            result.append(char)
    return result