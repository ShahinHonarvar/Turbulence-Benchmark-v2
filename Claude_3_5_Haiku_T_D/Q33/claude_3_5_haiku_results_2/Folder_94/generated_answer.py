def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = []
    for index in range(40, 94):
        if index < len(string):
            char = string[index]
            if char in vowels and '4' < char <= 'H':
                result.append(char)
    return result