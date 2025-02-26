def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(10, 97):
        if i < len(string):
            char = string[i]
            if char.lower() in vowels and 'R' < char <= 'b':
                result.append(char)
    return result