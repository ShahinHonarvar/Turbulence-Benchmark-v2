def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = []
    for index in range(44, 95):
        if index < len(string):
            char = string[index]
            if char in vowels and '5' < char <= '<':
                result.append(char)
    return result