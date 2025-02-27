def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in string[82:90]:
        if char > 'T' and char <= 'b' and (char in vowels):
            result.append(char)
    return result