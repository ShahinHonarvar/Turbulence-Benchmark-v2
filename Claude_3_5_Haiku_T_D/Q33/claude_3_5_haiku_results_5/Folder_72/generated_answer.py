def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = []
    for i in range(37, 57):
        if i < len(string):
            char = string[i]
            if char in vowels and char > '*' and (char <= 'P'):
                result.append(char)
    return result