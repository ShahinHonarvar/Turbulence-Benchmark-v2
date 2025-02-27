def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in string[11:53]:
        if char > '+' and char <= 'W' and (char in vowels):
            result.append(char)
    return result