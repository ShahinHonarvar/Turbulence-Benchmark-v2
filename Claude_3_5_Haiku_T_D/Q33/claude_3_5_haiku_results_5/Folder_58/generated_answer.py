def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = []
    for i in range(260, 322):
        if i < len(string):
            char = string[i]
            if char in vowels and char > '%' and (char <= 'U'):
                result.append(char)
    return result