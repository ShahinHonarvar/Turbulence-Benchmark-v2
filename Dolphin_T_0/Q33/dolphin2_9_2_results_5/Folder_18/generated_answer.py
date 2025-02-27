def return_vowels(s):
    vowels = ['A', 'E', 'I', 'O', 'U']
    result = []
    for index in range(528, 606):
        char = s[index]
        if char > 'M' and char <= 'X' and (char in vowels):
            result.append(char)
    return result