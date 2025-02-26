def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(21, 23):
        if i < len(string):
            char = string[i].lower()
            if char in vowels and '-' < char <= 'n':
                result.append(char)
    return result