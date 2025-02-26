def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = []
    for i in range(20, 41):
        if i < len(string):
            char = string[i]
            if char in vowels and 'K' < char <= 'Z':
                result.append(char)
    return result