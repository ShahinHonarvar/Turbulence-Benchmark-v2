def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for idx in range(28, 76):
        if idx < len(string):
            char = string[idx].lower()
            if char in vowels and '+' < char <= 'z':
                result.append(char)
    return result