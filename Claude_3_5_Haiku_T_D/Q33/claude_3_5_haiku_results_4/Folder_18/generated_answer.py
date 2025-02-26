def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = []
    for i in range(528, 606):
        if i < len(string):
            char = string[i]
            if char in vowels and 'M' < char <= 'X':
                result.append(char)
    return result