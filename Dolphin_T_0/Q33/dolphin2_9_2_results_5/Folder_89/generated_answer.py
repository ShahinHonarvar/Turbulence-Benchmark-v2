def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in string[50:51]:
        if char in vowels:
            result.append(char)
    return result