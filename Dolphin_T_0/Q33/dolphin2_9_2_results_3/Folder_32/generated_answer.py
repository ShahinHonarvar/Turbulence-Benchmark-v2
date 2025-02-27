def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    output = []
    for char in string[45:76]:
        if char > 'b' and char <= 'z' and (char in vowels):
            output.append(char)
    return output