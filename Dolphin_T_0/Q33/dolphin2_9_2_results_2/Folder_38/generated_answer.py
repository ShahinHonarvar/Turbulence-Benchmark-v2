def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in string[17:65]:
        if char > 'U' and char <= '{' and (char in vowels):
            result.append(char)
    return result