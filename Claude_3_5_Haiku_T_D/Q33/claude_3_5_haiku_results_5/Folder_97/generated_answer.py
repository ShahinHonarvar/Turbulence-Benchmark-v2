def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = []
    for index in range(328, 455):
        if index < len(string):
            char = string[index]
            if char in vowels and '<' < char <= 'z':
                result.append(char)
    return result