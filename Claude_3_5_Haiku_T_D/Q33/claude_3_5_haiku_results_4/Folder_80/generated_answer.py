def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for index in range(85, 99):
        if index < len(string):
            char = string[index].lower()
            if char in vowels and char > '/' and (char <= 'n'):
                result.append(char)
    return result