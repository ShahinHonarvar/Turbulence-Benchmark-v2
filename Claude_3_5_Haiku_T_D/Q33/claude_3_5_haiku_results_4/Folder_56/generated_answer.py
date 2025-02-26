def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = []
    for index in range(15, 86):
        if index < len(string):
            char = string[index]
            if char > '@' and char <= '~' and (char in vowels):
                result.append(char)
    return result