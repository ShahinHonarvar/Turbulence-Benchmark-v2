def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for index in range(46, 49):
        if index < len(string):
            char = string[index].lower()
            if char in vowels and '[' < char <= 'p':
                result.append(char)
    return result