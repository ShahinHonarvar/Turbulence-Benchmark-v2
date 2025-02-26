def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for index in range(14, 60):
        if index < len(string):
            char = string[index].lower()
            if char in vowels and 'd' < char <= 'v':
                result.append(char)
    return result