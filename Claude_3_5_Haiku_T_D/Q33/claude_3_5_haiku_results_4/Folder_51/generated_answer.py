def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = []
    for index in range(56, 68):
        if index < len(string):
            char = string[index]
            if char in vowels and 'M' < char <= 'X':
                result.append(char)
    return result