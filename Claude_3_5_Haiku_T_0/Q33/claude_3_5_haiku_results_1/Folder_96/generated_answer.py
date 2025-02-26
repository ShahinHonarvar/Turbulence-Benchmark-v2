def return_vowels(string):
    vowels = ['A', 'E', 'I', 'O', 'U']
    result = []
    for i in range(77, 84):
        if i < len(string):
            char = string[i]
            if char in vowels and '(' < char <= 'G':
                result.append(char)
    return result