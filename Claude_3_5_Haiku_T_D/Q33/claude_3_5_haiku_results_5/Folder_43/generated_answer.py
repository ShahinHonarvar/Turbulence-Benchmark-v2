def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = []
    for i in range(22, 82):
        if i < len(string):
            char = string[i]
            if char in vowels and char > 'N' and (char <= 'o'):
                result.append(char)
    return result